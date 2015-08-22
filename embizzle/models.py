from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, FloatField, ForeignKey, IntegerField, Model, OneToOneField
from django.utils import timezone

OTHER_STARVATION_UNREST = 10
BREEDER_STARVATION_UNREST = 50
CHILD_STARVATION_UNREST = 100


class Game(Model):
    started_at = DateTimeField(default=timezone.now)
    last_tick = DateTimeField(default=timezone.now)
    ticks = IntegerField(default=0)  # Each tick is one "cycle".
    tick_length = IntegerField(default=60)  # Length of each tick in seconds.

    def time_until_next_tick(self):
        return (self.last_tick + timedelta(seconds=self.tick_length)) - timezone.now()

    def check_tick(self):
        ticks_to_process = 0
        while self.time_until_next_tick() < timedelta(seconds=0):
            ticks_to_process += 1
            self.ticks += 1
            self.last_tick += timedelta(seconds=self.tick_length)
        print("processing {} ticks".format(ticks_to_process))
        self.save()
        self.process_ticks(ticks_to_process)

    def process_ticks(self, ticks):
        self.save()
        for leader in self.leaders.all():
            leader.process_ticks(ticks)


class Civilisation(Model):
    name = CharField(max_length=1024, default="Nowhere")
    funds = FloatField(default=1000.0)
    unrest = IntegerField(default=0)  # How unhappy the population are with their leader
    children = IntegerField(default=0)  # Number of children in the population
    breeders = IntegerField(default=100)  # People of breeding age / ability/ will
    others = IntegerField(default=20)  # Others
    birth_rate = FloatField(default=0.07)  # birth rate per breeder

    # Death rates
    children_death_rate = FloatField(default=0.002)  # death rate per child
    breeder_death_rate = FloatField(default=0.005)  # death rate per breeder
    other_death_rate = FloatField(default=0.1)  # death rate per other

    # Starvation tracking
    starved_children = IntegerField(default=0)
    starved_breeders = IntegerField(default=0)
    starved_others = IntegerField(default=0)

    tax_rate = FloatField(default=0.05)

    nutrients = IntegerField(default=1000)  # one consumed per person per tick
    nutrient_production = IntegerField(default=2)  # nutrients produced per breeder and pre 2 others.

    # Upgrade levels
    economy_level = IntegerField(default=0)
    healthcare_level = IntegerField(default=0)
    education_level = IntegerField(default=0)
    agriculture_level = IntegerField(default=0)

    def population(self):
        return self.children + self.breeders + self.others

    def process_ticks(self, ticks):
        for i in range(ticks):
            self.unrest += 1

            # Each cycle 1/20th of "children" become "breeders"
            if self.children > 0:
                education_mult = 1.0 + self.education_level / 200.0
                new_breeders = max(1, int(round(self.children / 20.0) * education_mult))
                self.breeders += new_breeders
                self.children -= new_breeders

            # Also 1/20th of "breeders" become "others"
            if self.breeders > 0:
                new_others = max(1, int(round(self.breeders / 20.0)))
                self.others += new_others
                self.breeders -= new_others

            # Produce new children based on birth rate
            if self.breeders > 2:
                self.children += max(1, int(round(self.breeders * self.birth_rate)))

            # Apply death rates
            healthcare_reduction = 1.0 - self.healthcare_level / 200.0
            self.children -= int(round(self.children * self.children_death_rate * healthcare_reduction))
            self.breeders -= int(round(self.breeders * self.breeder_death_rate * healthcare_reduction))
            self.others -= int(round(self.others * self.other_death_rate * healthcare_reduction))

            # Consume food/process starvation
            self.starved_children = self.starved_breeders = self.starved_others = 0

            agriculture_mult = 1.0 + self.agriculture_level / 200.0
            self.nutrients += self.nutrient_production * (self.breeders + self.others / 2) * agriculture_mult

            if self.nutrients >= self.population():
                self.nutrients -= self.population()
            else:
                starvation = self.population() - self.nutrients
                # TODO: Make this into a cleaner loop.
                if starvation > self.others:
                    self.others = 0
                    starvation -= self.others
                    self.starved_others = self.others
                    self.unrest += self.others * OTHER_STARVATION_UNREST
                    if starvation > self.breeders:
                        self.breeders = 0
                        self.starved_children = self.breeders
                        starvation -= self.breeders
                        self.unrest += self.breeders * BREEDER_STARVATION_UNREST
                        if starvation > self.children:
                            # uh oh
                            self.children = 0
                            self.starved_children = self.children
                            starvation -= self.children
                            self.unrest += self.children * CHILD_STARVATION_UNREST
                        else:
                            self.starved_children = starvation
                            self.children -= starvation
                            self.unrest += starvation * CHILD_STARVATION_UNREST
                    else:
                        self.starved_breeders = starvation
                        self.breeders -= starvation
                        self.unrest += starvation * BREEDER_STARVATION_UNREST
                else:
                    self.starved_others = starvation
                    self.others -= starvation
                    self.unrest += starvation * OTHER_STARVATION_UNREST

                self.nutrients = 0

            # Process funds
            economy_mult = 1.0 + self.economy_level / 1000.0
            self.funds += (self.breeders * self.tax_rate + self.others / 2 * self.tax_rate) * economy_mult

        if ticks:
            self.save()


class Leader(Model):
    game = ForeignKey(Game, related_name="leaders")
    name = CharField(max_length=1024, default="Someone")
    user = ForeignKey(User, related_name="leaders")
    civ = OneToOneField(Civilisation, related_name="leader")
    funds = FloatField(default=100.0)
    palace_size = IntegerField(default=1)  # How big this leader's "palace" is.

    def process_ticks(self, ticks):
        self.civ.process_ticks(ticks)

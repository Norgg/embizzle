from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, FloatField, ForeignKey, IntegerField, Model, OneToOneField
from django.utils import timezone


class Game(Model):
    started_at = DateTimeField(default=timezone.now)
    last_tick = DateTimeField(default=timezone.now)
    ticks = IntegerField(default=0)  # Each tick is one "cycle".
    tick_length = IntegerField(default=1)  # Length of each tick in seconds.

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
    funds = IntegerField(default=1000)
    unrest = IntegerField(default=0)  # How unhappy the population are with their leader
    children = IntegerField(default=0)  # Number of children in the population
    breeders = IntegerField(default=100)  # People of breeding age / ability/ will
    others = IntegerField(default=20)  # Others
    birth_rate = FloatField(default=0.07)  # birth rate per breeder
    children_death_rate = FloatField(default=0.002)  # death rate per child
    breeder_death_rate = FloatField(default=0.005)  # death rate per breeder
    other_death_rate = FloatField(default=0.1)  # death rate per other
    nutrients = IntegerField(default=1000)  # one consumed per person per tick
    nutrient_production = IntegerField(default=2)  # nutrients produced per breeder and pre 2 others.

    def population(self):
        return self.children + self.breeders + self.others

    def process_ticks(self, ticks):
        for i in range(ticks):
            self.unrest += 1

            # Each cycle 1/20th of "children" become "breeders"
            new_breeders = max(1, int(round(self.children / 20.0)))
            self.breeders += new_breeders
            self.children -= new_breeders

            # Also 1/20th of "breeders" become "others"
            new_others = max(1, int(round(self.breeders / 20.0)))
            self.others += new_others
            self.breeders -= new_others

            # Produce new children based on birth rate
            if self.breeders > 2:
                self.children += max(1, int(round(self.breeders * self.birth_rate)))

            # Apply death rates
            self.children -= int(round(self.children * self.children_death_rate))
            self.breeders -= int(round(self.breeders * self.breeder_death_rate))
            self.others -= int(round(self.others * self.other_death_rate))

            # Consume food/process starvation
            if self.nutrients >= self.population():
                self.nutrients -= self.population()
            else:
                starvation = self.population() - self.nutrients
                if starvation > self.others:
                    self.others = 0
                    starvation -= self.others
                    if starvation > self.breeders:
                        self.breeders = 0
                        starvation -= self.breeders
                        if starvation > self.children:
                            # uh oh
                            self.children = 0
                            starvation -= self.children
                        else:
                            self.children -= starvation
                    else:
                        self.breeders -= starvation
                else:
                    self.others -= starvation

                self.nutrients = 0
            self.nutrients += self.nutrient_production * (self.breeders + self.others / 2)

        if ticks:
            self.save()


class Leader(Model):
    game = ForeignKey(Game, related_name="leaders")
    name = CharField(max_length=1024, default="Someone")
    user = ForeignKey(User, related_name="leaders")
    civ = OneToOneField(Civilisation, related_name="leader")
    funds = IntegerField(default=100)

    def process_ticks(self, ticks):
        self.civ.process_ticks(ticks)

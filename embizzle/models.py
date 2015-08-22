from datetime import timedelta

from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, FloatField, ForeignKey, IntegerField, Model, OneToOneField
from django.utils import timezone


class Game(Model):
    started_at = DateTimeField(default=timezone.now)
    last_tick = DateTimeField(default=timezone.now)
    ticks = IntegerField(default=0)
    tick_length = IntegerField(default=20)  # Length of each tick in seconds.

    def time_until_next_tick(self):
        return (self.last_tick + timedelta(seconds=self.tick_length)) - timezone.now()

    def check_tick(self):
        while self.time_until_next_tick() < timedelta():
            self.tick()

    def tick(self):
        self.ticks += 1
        self.last_tick += timedelta(seconds=self.tick_length)
        self.save()
        for leader in self.leaders.all():
            leader.process_tick()
            leader.civ.process_tick()


class Civilisation(Model):
    name = CharField(max_length=1024)
    funds = IntegerField(default=1000)
    unrest = IntegerField(default=0)  # How unhappy the population are with their leader
    children = IntegerField(default=100)  # Number of children in the population
    breeders = IntegerField(default=100)  # People of breeding age
    others = IntegerField(default=100)  # Others
    birth_rate = FloatField(default=0.001)  # birth rate per thousand people
    death_rate = FloatField(default=0.002)  # death rate per thousand people

    def population(self):
        return self.children + self.breeders + self.others


class Leader(Model):
    game = ForeignKey(Game, related_name="leaders")
    name = CharField(max_length=1024)
    user = ForeignKey(User, related_name="leaders")
    civ = OneToOneField(Civilisation, related_name="leader")
    funds = IntegerField()

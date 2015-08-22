from django.contrib.auth.models import User
from django.db.models import CharField, DateTimeField, FloatField, ForeignKey, IntegerField, Model, OneToOneField
from django.utils import timezone


class Game(Model):
    last_tick = DateTimeField(default=timezone.now)


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
    game = ForeignKey(Game)
    user = ForeignKey(User)
    civ = OneToOneField(Civilisation)
    funds = IntegerField()

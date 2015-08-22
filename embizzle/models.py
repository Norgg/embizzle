from django.contrib.auth.models import User
from django.db.models import CharField, ForeignKey, IntegerField, Model, OneToOneField


class Civilisation(Model):
    name = CharField(max_length=1024)
    funds = IntegerField()
    population = IntegerField()


class Leader(Model):
    user = ForeignKey(User)
    civ = OneToOneField(Civilisation)
    funds = IntegerField()

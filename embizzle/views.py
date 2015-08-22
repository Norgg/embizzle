from django.shortcuts import render

from models import Civilisation, Game, Leader


def index(request):
    game, created = Game.objects.get_or_create(id=1)
    game.check_tick()
    civ = Civilisation(name="Norggland")
    leader = Leader(name="Norgg", game=game, civ=civ, funds=2000)
    return render(request, "index.html", locals())


def login(request):
    pass


def register(request):
    pass

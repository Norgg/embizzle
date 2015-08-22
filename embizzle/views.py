from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from models import Civilisation, Game, Leader


def index(request):
    user, _ = User.objects.get_or_create(id=1, username="Norgg")
    game, _ = Game.objects.get_or_create(id=1)
    game.check_tick()
    civ, _ = Civilisation.objects.get_or_create(id=1, name="Norggland")
    leader, _ = Leader.objects.get_or_create(id=1, name="Norgg", game=game, civ=civ, user=user)
    return render(request, "index.html", locals())


def login(request):
    pass


def register(request):
    pass


def reset(request):
    Leader.objects.all().delete()
    Civilisation.objects.all().delete()
    Game.objects.all().delete()
    return redirect(index)

import __init__

import actions

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from forms import RegistrationForm

from models import Civilisation, Game, Leader


def test_objs():
    user, _ = User.objects.get_or_create(id=1, username="Norgg")
    game, _ = Game.objects.get_or_create(id=1)
    civ, _ = Civilisation.objects.get_or_create(id=1, name="Norggland")
    leader, _ = Leader.objects.get_or_create(id=1, name="Norgg", game=game, civ=civ, user=user)
    return user, game, civ, leader


@login_required
def index(request):
    user, game, civ, leader = test_objs()
    game.check_tick()
    # game.process_ticks(1000)
    return render(request, "index.html", locals())


def login(request):
    pass


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print(form.data['password'])
    else:
        form = RegistrationForm()
    return render(request, "register.html", locals())


def action(request, action):
    added_keys = set(actions.__dict__.keys()) - set(__init__.__dict__.keys())
    user, game, civ, leader = test_objs()
    if action in added_keys:
        actions.__dict__[action](user, game, civ, leader)
    return redirect(index)


def reset(request):
    Leader.objects.all().delete()
    Civilisation.objects.all().delete()
    Game.objects.all().delete()
    return redirect(index)

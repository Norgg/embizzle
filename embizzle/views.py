import __init__

import actions

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render

from forms import RegistrationForm

from models import Civilisation, Game, Leader


@login_required
@transaction.atomic
def index(request):
    user = request.user
    leader = user.leaders.all()[0]
    civ = leader.civ
    game = leader.game
    game.check_tick()
    top_leaders = Leader.objects.order_by('-palace_size')[0:10]
    unrest_percent = int(civ.unrest * 100 / civ.max_unrest)
    return render(request, "index.html", locals())


@transaction.atomic
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            game, created = Game.objects.get_or_create(id=1)  # TODO: Handle game creation properly.
            user = User.objects.create(username=form.cleaned_data['leader_name'])
            civ = Civilisation.objects.create(name="The People of {}".format(form.cleaned_data['leader_name']))
            leader = Leader.objects.create(name=form.cleaned_data['leader_name'], user=user, civ=civ, game=game)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=form.cleaned_data['leader_name'],
                                password=form.cleaned_data['password'])
            login(request, user)
            print("User created.")
            return redirect(index)
    else:
        form = RegistrationForm()
    return render(request, "register.html", locals())


@login_required
def action(request, action):
    user = request.user
    leader = user.leaders.all()[0]
    civ = leader.civ
    game = leader.game
    added_keys = set(actions.__dict__.keys()) - set(__init__.__dict__.keys())
    if action in added_keys:
        actions.__dict__[action](user, game, civ, leader)
    return redirect(index)


@user_passes_test(lambda u: u.is_superuser)
def reset(request):
    Leader.objects.all().delete()
    Civilisation.objects.all().delete()
    Game.objects.all().delete()
    return redirect(index)

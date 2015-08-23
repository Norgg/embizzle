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
    leader = Leader.objects.filter(user=user).select_related('game')[0]
    game = leader.game
    game.check_tick()
    leader = Leader.objects.filter(user=user).select_related('civ')[0]
    civ = leader.civ
    top_leaders = Leader.objects.order_by('-palace_size')[0:10]
    unrest_percent = int(civ.unrest * 100 / civ.max_unrest)
    nutrient_percent = int(civ.nutrients * 100 / civ.nutrient_storage)
    palace_rows = [leader.palace[i:i+16] for i in range(0, len(leader.palace), 16)]
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


@login_required
def build(request, row, column):
    user = request.user
    leader = user.leaders.all()[0]
    if leader.palace_blocks > 0:
        leader.palace_blocks -= 1
        leader.palace_size += 1
        palace_list = list(leader.palace)
        palace_list[16*(int(row)-1) + (int(column)-1)] = '#'
        leader.palace = "".join(palace_list)
    leader.save()
    return redirect(index)


@user_passes_test(lambda u: u.is_superuser)
def reset(request):
    Leader.objects.all().delete()
    Civilisation.objects.all().delete()
    Game.objects.all().delete()
    return redirect(index)

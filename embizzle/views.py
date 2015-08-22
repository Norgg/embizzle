from django.shortcuts import render

from models import Civilisation, Leader


def index(request):
    civ = Civilisation(name="Norggland")
    leader = Leader(civ=civ, funds=2000)
    return render(request, "index.html", locals())


def login(request):
    pass


def register(request):
    pass

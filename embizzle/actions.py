from random import random

from models import Civilisation, Leader

from roman import toRoman

titles = ['the Glorious', 'the Great', 'the Transcendent', 'the Beautiful', 'the Dark',
          'the Masterful', 'the Magnificent', 'the Wonderful', 'the Marvelous', 'the Invincible',
          'the Cruel', 'the Nice', 'the "Nice"', 'the Incandescent', 'the Powerful', 'the Brave',
          'the Ambivalent', 'the Bored', 'the Ambitious', 'the Apathetic']


def embezzle(user, game, civ, leader):
    if civ.funds >= 10:
        civ.unrest += max(5, (civ.funds / 100) ** 1.5)
        leader.funds += civ.funds
        civ.funds = 0
        civ.save()
        leader.save()


def raise_taxes(user, game, civ, leader):
    if civ.tax_rate < 0.99:
        civ.tax_rate += 0.1
        civ.unrest += 20
        civ.save()


def construct(user, game, civ, leader):
    while leader.funds >= 100:
        leader.funds -= 100
        leader.palace_blocks += 1
    leader.save()


def import_nutrients(user, game, civ, leader):
    if civ.funds >= 100:
        civ.nutrients += 100
        civ.funds -= 100
        civ.save()


def invest_economy(user, game, civ, leader):
    while civ.funds >= 100:
        civ.economy_level += 1
        civ.funds -= 100
    civ.save()


def invest_healthcare(user, game, civ, leader):
    while civ.funds >= 100:
        civ.healthcare_level += 1
        civ.funds -= 100
    civ.save()


def invest_agriculture(user, game, civ, leader):
    while civ.funds >= 100:
        civ.agriculture_level += 1
        civ.funds -= 100
    civ.save()


def reincarnate(user, game, civ, leader):
    new_title = titles[int(random() * len(titles))]
    new_name = "{} {} {}".format(user.username, toRoman(user.leaders.count() + 1), new_title)
    new_civ = Civilisation.objects.create(name="The People of {}".format(new_name))
    Leader.objects.create(name=new_name, user=user, civ=new_civ, game=game)

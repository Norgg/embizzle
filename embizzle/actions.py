def embezzle(user, game, civ, leader):
    print("embezzling")
    if civ.funds >= 100:
        civ.funds -= 100
        civ.unrest += 10
        leader.funds += 100
        civ.save()
        leader.save()


def raise_taxes(user, game, civ, leader):
    if civ.tax_rate < 1.0:
        civ.tax_rate += 0.01
        civ.unrest += 10
        civ.save()


def construct(user, game, civ, leader):
    if leader.funds >= 100:
        leader.funds -= 100
        leader.palace_size += 1
        leader.save()


def import_nutrients(user, game, civ, leader):
    if civ.funds >= 100:
        civ.nutrients += 100
        civ.funds -= 100
        civ.save()


def invest_economy(user, game, civ, leader):
    if civ.funds >= 100:
        civ.economy_level += 1
        civ.funds -= 100
        civ.save()


def invest_healthcare(user, game, civ, leader):
    if civ.funds >= 100:
        civ.healthcare_level += 1
        civ.funds -= 100
        civ.save()


def invest_education(user, game, civ, leader):
    if civ.funds >= 100:
        civ.education_level += 1
        civ.funds -= 100
        civ.save()


def invest_agriculture(user, game, civ, leader):
    if civ.funds >= 100:
        civ.agriculture_level += 1
        civ.funds -= 100
        civ.save()

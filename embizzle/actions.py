def embezzle(user, game, civ, leader):
    print("embezzling")
    if civ.funds >= 100:
        civ.funds -= 100
        leader.funds += 100
        civ.save()
        leader.save()


def construct(user, game, civ, leader):
    if leader.funds >= 100:
        leader.funds -= 100
        leader.palace_size += 1
        leader.save()

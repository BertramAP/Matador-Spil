#eksempel

def fødselsdags_gave(player, pulledid, data):
    if player.id == pulledid:
        player.cash += 10*nplayers-10
    else:
        player.cash -= 10
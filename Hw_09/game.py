total = 150
game = False


def get_total():
    global total
    return total


def take_candy(take: int):
    global total
    total -= take


def new_game():
    global game
    global total
    if game:
        game = False
    else:
        total = 150
        game = True


def get_game():
    global game
    return game

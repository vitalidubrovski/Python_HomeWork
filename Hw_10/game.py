max_total = 150
total = max_total
game = False
difficulty = 'Easy'


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
        total = max_total
        game = True


def get_game():
    global game
    return game


def set_max_total(value: int):
    global max_total
    max_total = value


def change_difficulty():
    global difficulty
    if difficulty == 'Easy':
        difficulty = 'Hard'
    else:
        difficulty = 'Easy'


def get_difficulty():
    global difficulty
    return difficulty

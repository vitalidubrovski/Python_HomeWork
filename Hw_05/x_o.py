# Создайте программу для игры в ""Крестики-нолики"".


board = list(range(1, 10))


def field(cell: list):
    print('-' * 13)
    for i in range(3):
        print(f'| {cell[0 + i * 3]} | {cell[1 + i * 3]} | {cell[2 + i * 3]} |')
        print('-' * 13)


def take_input(x_or_o):
    valid = False
    while not valid:
        player_answer = input('Куда поставим ' + x_or_o + ' ? ')
        try:
            player_answer = int(player_answer)
        except:
            print('Вы уверены что ввели число? Введите от 1 до 9')
            continue
        if (player_answer >= 1) and (player_answer <= 9):
            if (str(board[player_answer - 1])) not in 'XO':
                board[player_answer - 1] = x_or_o
                valid = True
            else:
                print('Клетка уже занята.')
        else:
            print('Введите число от 1 до 9, чтобы походить.')


def check_win(board: list):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_coord:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False


def main(board: list):
    counter = 0
    win = False
    while not win:
        field(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    field(board)


main(board)

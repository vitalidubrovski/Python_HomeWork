# Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой.За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Подумайте как наделить бота ""интеллектом""

from random import randint

player1 = input('Введите имя игрока: ')
player2 = 'Bot'
value = 150


def take_amount(name):
    input_data = int(input(f' {name} Введите количество конфет, которые хотите взять от 1 до 28: '))
    while input_data < 1 or input_data > 28:
        input_data = input(f'{name} Введите корректное количество. ')
    return input_data


def score_print(name, amount, count, value):
    print(f'Ходил {name}, взял {amount}, теперь у него {count}. На столе осталось {value} конфет. ')


def some_mind(value):
    amount = randint(1, 29)
    while value - amount <= 28 and value > 28:
        amount = randint(1, 29)
    return amount


def main(value):
    turn = randint(0, 2)
    if turn:
        print(f'Первым ходит {player1}')
    else:
        print(f'Первым ходит {player2}')
    count1 = 0
    count2 = 0
    while value > 28:
        if turn:
            amount = take_amount(player1)
            count1 += amount
            value -= amount
            turn = False
            score_print(player1, amount, count1, value)
        else:
            amount = some_mind(value)
            count2 += amount
            value -= amount
            turn = True
            score_print(player2, amount, count2, value)

    if turn:
        print(f'Победил {player1}')
    else:
        print(f'Победил {player2}')


if __name__ == '__main__':
    main(value)

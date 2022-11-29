# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод
import random

size = int(input('Введите размер списка: '))


def shuffle(number):
    my_list = []
    for i in range(size):
        my_list.append(random.randint(0, 21))
    print(my_list)
    temp = 0
    for i in range(len(my_list)):
        j = random.randint(i, len(my_list)) - 1
        if my_list[i] != my_list[j]:
            temp = my_list[j]
            my_list[j] = my_list[i]
            my_list[i] = temp
    return my_list


print(shuffle(size))

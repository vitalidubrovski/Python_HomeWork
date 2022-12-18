# Пройтись по своим предыдущим ДЗ и где возможно использовать ускореную обработку данных
# (достаточно 3 примеров)
import random

# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
n = int(input('Введите число: '))
my_list = [(1 + 1 / i) ** i for i in range(1, n + 1)]
suma = 0
# for i in range(1, n + 1):
#     my_list.append((1 + 1 / i) ** i)
for i in my_list:
    suma += i

print(my_list)
print(f'{suma:.2f}')

# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
size = int(input('Введите размер списка: '))
my_list = [random.randint(1, 21) for i in range(size)]
# for i in range(size):
#     my_list.append(random.randint(1, 21))
print(my_list)
total = 0
for i in range(1, len(my_list), 2):
    total += my_list[i]
    print(my_list[i])
print(f'Сумма элементов на нечетных индексах: {total}')


# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

# size = int(input('Введите размер списка: '))


def shuffle(number):
    my_list = [random.randint(0, 21) for i in range(size)]
    # for i in range(size):
    #     my_list.append(random.randint(0, 21))
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

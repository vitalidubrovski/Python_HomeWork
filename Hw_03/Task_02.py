# Напишите программу,
# которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]
import random

size = int(input('Введите размер массива: '))
my_list = []
for i in range(size):
    my_list.append(random.randint(1, 11))
print(my_list)
valid_list = []
left = 0
while left < size / 2:
    right = (left + 1) * -1
    valid_list.append(my_list[left] * my_list[right])
    left += 1
print(valid_list)



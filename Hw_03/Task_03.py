# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

my_max = my_list[0] % 1
my_min = my_list[0] % 1

for i in range(len(my_list)):
    if my_list[i] % 1 > my_max:
        my_max = my_list[i]
    elif my_list[i] % 1 < my_min:
        my_min = my_list[i]

print(f'{round(my_max % 1, 2) - round(my_min % 1, 2)}')

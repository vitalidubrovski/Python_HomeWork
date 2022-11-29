# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
n = int(input('Введите число: '))
my_list = []
suma = 0
for i in range(1, n + 1):
    my_list.append((1 + 1 / i) ** i)
for i in my_list:
    suma += i

print(my_list)
print(f'{suma:.2f}')

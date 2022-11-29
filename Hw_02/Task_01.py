# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

numbers = float(input('Введите вещественное число: '))


def summa_1(n):
    suma = 0
    for digit in str(numbers):
        if digit.isdigit():
            suma += int(digit)
    return suma


def summa_2(n):
    suma = 0
    n = str(n).replace(',', '.')
    n = n.split('.')
    for i in range(len(n)):
        digit = int(n[i])
        while digit != 0:
            suma += digit % 10
            digit //= 10
    return suma


print(summa_1(numbers))
print(summa_2(numbers))

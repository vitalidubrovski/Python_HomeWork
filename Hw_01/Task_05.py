# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве
# (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расcтояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
from math import sqrt
import random

print('Задача 5')
a_x = random.randint(1, 11)
a_y = random.randint(1, 11)
b_x = random.randint(1, 11)
b_y = random.randint(1, 11)
print(
    f'Точка А с координатами ({a_x},{a_y})\n Точка B с координатами ({b_x},{b_y})')
result = sqrt((a_x - b_x)**2 + (a_y - b_y)**2)
result = complex(round(result.real, 2), round(result.imag))
print('Расстояние: {}'.format(result), end='\n')

# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# # если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

degree1 = int(input('Введите натуральную степень многочлена: '))
degree2 = int(input('Введите натуральную степень второго многочлена: '))


def fill_polynomial(degree) -> dict:
    koef = {}
    for i in range(degree + 1):
        koef[i] = random.randint(0, 100)
    return koef


first_polynom = fill_polynomial(degree1)
second_polynom = fill_polynomial(degree2)


def get_polynomial(koef: dict) -> str:
    polynomial = ''
    for i in range(len(koef) - 1, -1, -1):
        if koef[i] != 0:
            if koef[i] == 1:
                if i == 1:
                    polynomial += f'x + '
                elif i == 0:
                    polynomial += f'1 '
                else:
                    polynomial += f'x^{i} + '
            else:
                if i == 1:
                    polynomial += f'{koef[i]}*x + '
                elif i == 0:
                    polynomial += f'{koef[i]} '
                else:
                    polynomial += f'{koef[i]}*x^{i} + '

    return polynomial + '= 0'


print(get_polynomial(first_polynom))
print(get_polynomial(second_polynom))


def parse_polynomial(polynom: str) -> dict:
    polynom = polynom.replace(' = 0', '').replace(' + ', ' ').split(' ')
    result = []
    for item in polynom:
        if not 'x' in item:
            result.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    result.append(['1', '1'])
                else:
                    result.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    result.append(('1' + item).split('x^'))
                else:
                    result.append(item.split('*x^'))
    print(result)
    polynomial_dict = {}
    for item in result:
        polynomial_dict[int(item[1])] = int(item[0])
    return polynomial_dict


parse_polynomial(get_polynomial(first_polynom))
parse_polynomial(get_polynomial(second_polynom))


def sum_of_polynomial(first: dict, second: dict) -> dict:
    valid = {}
    valid.update(first)
    valid.update(second)
    for key in valid:
        if first.get(key) and second.get(key):
            valid[key] = first.get(key) + second.get(key)
        elif first.get(key):
            valid[key] = first.get(key)
        else:
            valid[key] = second.get(key)
    return dict(sorted(valid.items())[::-1])


result = sum_of_polynomial(first_polynom, second_polynom)
print(get_polynomial(result))

with open('Polynomial_1.txt', 'w', encoding='utf-8') as data1:
    data1.write(get_polynomial(first_polynom))

with open('Polynomial_2.txt', 'w', encoding='utf-8') as data2:
    data2.write(get_polynomial(second_polynom))

with open('Polynomial_summ.txt', 'w', encoding='utf-8') as result_data:
    result_data.write(get_polynomial(result))

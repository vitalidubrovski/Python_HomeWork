# Кирилл, это было невероятно, спасибо тебе большое за твой вклад в развитие таких тугодумов как я).
# Не скажу, что усвоено все, что мы здесь прошли, но какая-то часть, прям до щелчка внутри.
# Ты очень крутой ментор и преподаватель, которому не наплевать на своих учеников. Низкий тебе поклон :)
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

limit = 100
step = 0.01
x = np.arange(-limit, limit, step)
a, b, c, d, e = -12, - 18, 10, 5, - 30
color = 'r'
line = '-.'
grow = True
x_change = {-limit: 'Grow'}


def f(x):
    function = a * x ** 4 * np.sin(np.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return function


def switch_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


def switch_line():
    global line
    if line == '-.':
        line = '-'
    else:
        line = '-.'
    return line


x_min = -limit
f_min = f(-limit)

for x_cur in x:
    if f(x_cur) < x_min:
        f_min = np.round(f(x_cur), 2)
        x_min = np.round(x_cur, 2)

print(x_min, f_min)

for i in range(len(x) - 1):
    if (f(x[i]) <= 0 or f(x[i + 1]) >= 0) and not f(x[i] < 0 and f(x[i + 1]) > 0):
        x_change[x[i]] = 'zero'
    if grow:
        if f(x[i]) > f(x[i + 1]):
            grow = False
            x_change[x[i]] = 'Grow'
    else:
        if f(x[i]) < f(x[i + 1]):
            grow = True
            x_change[x[i]] = 'Grow'

x_change[limit] = 'Grow'
print(x_change)

x_keys = [x for x in x_change]
x_keys.sort()
print(x_keys)

for i in range(len(x_keys) - 1):
    x_cur = np.arange(x_keys[i], x_keys[i + 1] + step, step)
    if x_change.get(x_keys[i]) == 'zero':
        switch_line()
    else:
        switch_color()
    plt.rcParams['lines.linestyle'] = line
    plt.plot(x_cur, f(x_cur), color)

plt.show()

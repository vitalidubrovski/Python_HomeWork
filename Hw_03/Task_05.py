# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов (Негафибоначчи).
# Пример: для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input('Введите число: '))


def fibonacci(n: int):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        list_1 = fibonacci(n - 1)
        list_1.append(list_1[-1] + list_1[-2])
    return list_1


def neg_fib(n: int):
    fib = fibonacci(n)
    result = fib[::-1] + [0] + fib
    for i in range(len(result) - n):
        if i % 2 == 0:
            result[i] *= -1
    print(result)


neg_fib(N)



# Совсем не понял как рекурсивно сделать вот по этой функции:
# Fn = F(n+2)−F(n+1). F−n = (−1)^n+1 * Fn. если не сложно подскажи пожалуйста
# По-цигански решил, хотелось бы красивое увидеть

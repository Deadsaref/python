from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


try:
    n = int(input('Введите число, до которого будем считать факториалы: '))
except ValueError:
    print('Введено не число')
else:
    for el in fact(n):
        print(el)

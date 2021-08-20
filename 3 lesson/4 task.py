def my_func(x, y):
    if x > 0 and y < 0 and type(y) == int:
        # y = abs(y)
        result_1 = x**y
        print(f'Результат первым способом {result_1}')

        ''' Второй способ без оператора ** через дополнительную переменную z'''
        z = x
        for i in range(y-1):
            z *= x
        result_2 = z
        print(f'Результат вторым способом {result_2}')
    else:
        print('Первое число должно быть положительным, а второе - целым отрицательным')


my_func(4, -2)
my_func(7, -10.2)
my_func(7, -5)
my_func(-2, -2)


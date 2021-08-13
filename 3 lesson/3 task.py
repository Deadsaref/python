def my_func(x1, x2, x3):
    filter_list = [x1, x2, x3]
    filter_list.remove(min(filter_list))
    print(float(filter_list[0] + filter_list[1]))


my_func(100, 2, 53)

# Не совсем понял формулировку (опять), поэтому задал аргументы при вызове функции, но можно раскомментировать код
# и вводить числа самому

# def my_func(x1=None, x2=None, x3=None):
#     x1 = int(input('Введите первое число: '))
#     x2 = int(input('Введите второе число: '))
#     x3 = int(input('Введите третье число: '))
#     filter_list = [x1, x2, x3]
#     filter_list.remove(min(filter_list))
#     print(float(filter_list[0] + filter_list[1]))
#
#
# my_func()

# добавил float для возможности вызова функции без введения аргументов
# т.к. не понял, как добавить поз. аргументы чтобы при этом "числа запрашивались у пользователя"
def divide(n1=float, n2=float):
    n1 = float(input('Введите делимое: '))
    n2 = float(input('Введите делитель: '))
    try:
        result = n1 / n2
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    else:
        return result


print(divide())

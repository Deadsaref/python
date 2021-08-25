class ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError('Деление на ноль запрещено')
            return x / y
    except ZeroDivisionError:
        print('Деление на ноль запрещено. Введите другой делитель')


division(10, 0)

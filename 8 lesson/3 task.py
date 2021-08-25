class ListError(Exception):
    def __init__(self, txt):
        self.txt = txt


def check():
    list = []
    while True:
        a = input('Введите число для добавления в список\nДля выхода введите "stop"')
        if a == 'stop':
            break
        if not a.isdigit():
            raise ListError('Введенное не является числом')
        list.append(a)
    print(list)


check()

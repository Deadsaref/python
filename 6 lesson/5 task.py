class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка ручкой {self.title}')


class Pencil(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка карандашом {self.title}')


class Handle(Stationery):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Отрисовка маркером {self.title}')


pen = Pen('Р-1')
pencil = Pencil('К-2')
handle = Handle('М-3')

pen.draw()
pencil.draw()
handle.draw()

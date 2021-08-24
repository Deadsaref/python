class Cell:
    def __init__(self, quantity):
        self.qua = quantity
        self.symbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.qua}')

    def __add__(self, other):
        return Cell(abs(self.qua + other.qua))

    def __mul__(self, other):
        return Cell(self.qua * other.qua)

    def __sub__(self, other):
        return Cell(abs(self.qua - other.qua))

    def __truediv__(self, other):
        return Cell(self.qua // other.qua)

    def make_order(self, count):
        x = self.qua
        while x > 0:
            for k in range(1, count + 1):
                print(self.symbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


a = Cell(5)
b = Cell(10)
c = Cell(3)
d = Cell(2)

print(a + b)
print(a - b)
print(a * b)
print(c / d)

a.make_order(3)
b.make_order(3)

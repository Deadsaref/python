class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)

    def __str__(self):
        if self.b > 0:
            sign = '+'
        else:
            sign = ''
        return f'c = {self.a}{sign}{self.b}i'


a = ComplexNumber(4, 6)
b = ComplexNumber(5, -3)
print(a + b)
print(a * b)

from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def need(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Cloth):

    @property
    def need(self):
        return self.param / 6.5 + 0.5


class Costume(Cloth):
    @property
    def need(self):
        return self.param * 2 + 0.3


coat = Coat(48)
costume = Costume(1.82)
# print(costume)
print(coat.need)
print(costume.need)

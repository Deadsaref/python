class Road:
    __length = None
    __width = None

    def __init__(self, length, width, weight=25, thickness=2):
        self.__length = length
        self.__width = width
        self.__weight = weight
        self.__thickness = thickness

    def mass(self):
        mass = float(self.__length * self.__width * self.__weight * self.__thickness) / 1000
        print(f'Для постройки дороги необходимо {mass} тонн асфальта')


a = Road(30, 5000)
a.mass()

b = Road(37, 12000, 32, 4)
b.mass()

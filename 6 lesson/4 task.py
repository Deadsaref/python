class Car:

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def show_speed(self):
        return f'Текущая скорость {self.name} составляет {self.speed} км/ч'

    def route(self):
        print(f'{self.go()}\n{self.show_speed()}\n{self.turn_left()}\n' \
              f'{self.turn_right()}\nЦвет {self.name} - {self.color}\n' \
              f'{self.stop()}')
        if hasattr(self, 'is_police') and self.is_police:
            print('Машина полицейская')


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч\n' \
                   f'!!! Превышение скорости на {abs(self.max_speed - self.speed)} км/ч'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч\n' \
                   f'{self.name} движется с нормальной скоростью'

    max_speed = 60


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > self.max_speed:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч\n' \
                   f'!!! Превышение скорости на {abs(self.max_speed - self.speed)} км/ч'
        else:
            return f'Текущая скорость {self.name} составляет {self.speed} км/ч\n' \
                   f'{self.name} движется с нормальной скоростью'

    max_speed = 40


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = is_police


def separator():
    print('-' * 20)


audi = TownCar(100, 'Черный', 'Ауди')
audi.route()
separator()

kangoo = WorkCar(40, 'Белый', 'Кенгу')
kangoo.route()
separator()

porshe = SportCar(200, 'Синий', 'Порше')
porshe.route()
separator()

ford = PoliceCar(80, 'Белый', 'Машина с мигалками', True)
ford.route()

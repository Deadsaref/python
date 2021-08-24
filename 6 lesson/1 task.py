from time import sleep


class TrafficLight:
    __color = None
    __colors = ['Красный', 'Желтый', 'Зеленый']

    def __init__(self):
        self.i = 0
        self.prev_i = -1
        self.__hidden_i = 0

    def running(self):
        print('Светофор включен')
        while True:
            self.__color = self.__colors[self.i]
            print(f'Цвет: {self.__color}')
            if self.i - self.prev_i == 1:
                self.prev_i = self.i
                self.i += 1
                if self.__color == 'Красный':
                    sleep(7)
                elif self.__color == 'Желтый':
                    sleep(2)
                elif self.__color == 'Зеленый':
                    self.i = 0
                    self.prev_i = -1
                    self.__hidden_i += 1
                    sleep(4)

                if self.__hidden_i == 2:
                    # здесь вшита поломка светофора после двух полных циклов
                    self.i = 1
            else:
                print('Нарушение алгоритма переключение светофора. Выключение')
                sleep(3)
                break
        print('Светофор выключен')


t = TrafficLight()
t.running()

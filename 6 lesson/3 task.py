class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'оклад': wage, 'премия': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus=0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_full_profit(self):
        return self._income.get('оклад') + self._income.get('премия')


w1 = Position('Алексей', 'Пронченко', 'младший аналитик', 30000)
w2 = Position('Михаил', 'Шац', 'аналитик', 50000, 15000)
w3 = Position('Олеся', 'Гринкевич', 'старший аналитик', 70000, 20000)

print(w1.get_full_name(), w1.get_full_profit())
print(w2.get_full_name(), w2.get_full_profit())
print(w3.get_full_name(), w3.get_full_profit())
class Date:
    def __init__(self, date):
        self.date_string = date

    def __str__(self):
        return self.date_string

    @classmethod
    def transform(cls, date):
        print(*map(int, date.date_string.split('-')))

    @staticmethod
    def validate(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:
                    return f'Дата верна'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            f'Неправильный день'


today = Date('25-08-2021')
print(today)
Date.transform(today)
print(Date.validate(25, 8, 2021))

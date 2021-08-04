# Cделал ввод аргументов в формате input, но механизм указывания данных в самой функции понятен
# просто имхо - менее изящный
def user(name=None, surname=None, year=None, city=None, email=None, phone=None):
    name = input('Введите имя: \n')
    surname = input('Введите фамилию: \n')
    while year is None:
        try:
            year = int(input('Введите год рождения: \n'))
        except ValueError:
            print('Укажите год рождения числом (пример 1996)')
    city = input('Введите город проживания: \n')
    email = input('Укажите свой e-mail: \n')
    while phone is None:
        try:
            phone = int(input('Укажите свой номер телефона: \n'))
        except ValueError:
            print('Неверный формат телефона')

    return name, surname, year, city, email, phone


print(user())

year_list = ['зима', 'весна', 'лето', 'осень']
month = int(input('Введите число месяца от 1 до 12: '))
while not (1 <= month <= 12):
    month = int(input('Неправильное число. Введите число месяца от 1 до 12: '))
if 1 <= month <= 2 or month == 12:
    result_l = year_list[0]
elif 3 <= month <= 5:
    result_l = year_list[1]
elif 6 <= month <= 8:
    result_l = year_list[2]
elif 9 <= month <= 11:
    result_l = year_list[3]

print(f'Сезон по списку: {result_l}')

year_dict = {
    'зима': (12, 1, 2),
    'весна': (3, 4, 5),
    'лето': (6, 7, 8),
    'осень': (9, 10, 11)
}

for season in year_dict.keys():
    if month in year_dict[season]:
        result_d = season

print(f'Сезон по словарю: {result_d}')

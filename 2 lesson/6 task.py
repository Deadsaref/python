products = []
analytics = {'название': [], 'цена': [], 'количество': [], 'ед. изм.': []}
features = {'название': '', 'цена': '', 'количество': '', 'ед. изм.': ''}
number = 1

while input('Хотите добавить новый товар? ') == 'да':
    for f in features.keys():
        feature = input(f'Введите параметр "{f}": ')
        features[f] = int(feature) if (f == 'цена' or f == 'количество') else feature
        analytics[f].append(features[f])
    products.append((number, features.copy()))
    # в предыдущей строчке без .copy не получается, хотя смотрел несколько других работ,
    # где справляются без этого, прокомментируйте ошибку
    number += 1
print('Список товаров')
for item in products:
    print(item)
print(f'\nАналитика по всем товарам:')
for key, value in analytics.items():
    print(f'{key}: {value}')


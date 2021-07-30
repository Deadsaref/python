input_string = input('Введите элементы через запятую: ')
list = input_string.split(',')
i = 0
while list:
    if i == len(list):
        break
    elif len(list) % 2 != 0 and i == len(list) - 1:
        break
    else:
        list[i], list[i+1] = list[i+1], list[i]
        i += 2

print(list)
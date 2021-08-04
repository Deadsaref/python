

def my_func():
    total = 0
    while True:
        summary = 0
        numbers = input('Для выхода из программы введите "#"\nВведите числа: ')
        numbers = numbers.split(' ')

        for i in numbers:
            if i == '#':
                print('Работа программы завершена')
                break
            elif i.isdigit():
                summary = summary + float(i)
            else:
                print('Введены неверные данные. Введите числа через пробел')
                continue

        print(f'Сумма введённых чисел - {summary}')
        total = total + summary
        if numbers[-1] == '#':
            break

    print(f'Сумма всех чисел за цикл - {total}')


my_func()
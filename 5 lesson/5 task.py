# не понял формулировку. Программно записать числа - это предусмотреть ввод чисел пользователем
# или вписать числа внутри кода?
# также добавил чтение чисел из файла по условиям задачи, а не из исходного пула чисел, для наглядности разделил
# код на две программы

with open('5_task.txt', 'w') as f:
    while True:
        try:
            line = list(map(float, input('Введите числа через пробел:\n').split()))
        except ValueError:
            print('Введён неверный формат данных')
        else:
            for i in line:
                f.write(str(i) + ' ')
            print('Запись чисел в файл успешна')
            break

with open('5_task.txt', 'r') as f2:
    inline = f2.read().split()
    print(f'Сумма чисел в файле = {sum(map(float, inline))}')

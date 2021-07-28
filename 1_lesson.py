def sep():
    print('='*10)

# sep()
# print('1 задание')
# sep()
#
# simple_a = 10
# simple_b = 'двадцать'
# simple_c = [1, 2, 3, 4]
# another_a = int(input('Введите любое число: '))
# another_b = input('Введите любое число прописью: ')
# another_c = input('Введите любое слово: ')
#
# print(f'{simple_a}\n{simple_b}\n{simple_c}')
# print(f'{another_a}\n{another_b}\n{another_c}')



# sep()
# print('2 задание')
# sep()
#
# # решил не заморачиваться с расчётом секунд и костылями на ограничением значений секунд и минут
# import datetime
#
# time = int(input('Введите время в секундах: '))
# print(str(datetime.timedelta(seconds=time)))



# sep()
# print('3 задание')
# sep()
#
# number = int(input('Введите число: '))
# print(number + number * 11 + number * 111)



# sep()
# print('4 задание')
# sep()
#
# find_max = None
#
#
# while True:
#     try:
#         find_max = int(input('Введите целое положительное число: '))
#         if find_max <= 0:
#             raise ValueError
#         break
#     except ValueError:
#         print('Введён неправильный формат числа')
#
# find_list = list(map(int, str(find_max)))
#
# print(f'Наибольшее число: {max(find_list)}')



# sep()
# print('5 задание')
# sep()
#
# earnings = int(input('Введите сумму выручки (тыс. руб.): '))
# costs = int(input('Введите сумму расходов (тыс. руб.): '))
#
# if earnings > costs:
#     print('Фирма прибыльна')
#     rentability = earnings / costs
#     print(f'Рентабельность: {rentability}')
#     people = int(input('Сколько работников в штате сейчас? '))
#     print(f'Прибыль в расчете на одного сотрудника: {earnings / people}  (тыс. руб.)')
# elif earnings == costs:
#     print('Фирма работает в 0')
# else:
#     print('Фирма убыточна')



# sep()
# print('6 задание')
# sep()
#
# initial_dist = float(input('С какой дистанции начинаем? '))
# final_dist = float(input('Какой результат нужен? '))
# day = 1
#
# while initial_dist < final_dist:
#     initial_dist = round(initial_dist * 1.1, 1)
#     #print(f'{day} день: {initial_dist} км.')
#     day += 1
#
# print(f'На {day}-й день спортсмен достиг результата — не менее {round(final_dist)} км.')
from itertools import count, cycle

for el in count(5):
    if el > 100:
        print('Цикл завершен')
        break
    else:
        print(el)

my_list = ['раз', 'два', 'три']
i = 0
for el in cycle(my_list):
    if i > 8:
        print('Цикл завершен')
        break
    else:
        print(el)
        i +=1
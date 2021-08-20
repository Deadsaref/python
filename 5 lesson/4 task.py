translator = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
new_list = []
with open('4_task.txt', 'r', encoding='utf-8') as f:
    for i in f:
        i = i.split(' ')
        print(i)
        new_list.append(translator[i[0]] + ' - ' + i[2])

with open('4_task_new.txt', 'w', encoding='utf-8') as f2:
    f2.writelines(new_list)

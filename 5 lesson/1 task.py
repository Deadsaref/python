with open('1_task.txt', 'w+') as f:
    line = 'None'
    while line:
        line = input('Введите строку: ')
        f.writelines(line + '\n')
        if not line:
            break
    f.seek(0)
    print(f.readlines())

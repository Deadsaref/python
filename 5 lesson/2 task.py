with open('2_task.txt', 'r', encoding='UTF-8') as f:
    content = f.readlines()
    lines = len(content)
    words = 0
    i = 1
    for line in content:
        line = line.split(' ')
        # print(line)
        words = len(line)
        print(f'Количество слов в {i} строке - {words}')
        i += 1

    print(f'Количество строк в файле - {lines}')

# в этом варианте символы, такие как "-" считаются за слово.
# Для решения, как я понял, надо освоить регулярные выражения

with open('3_task.txt', 'r', encoding='utf-8') as f:
    workers = f.read().split('\n')
    low = []
    total = []
    for worker in workers:
        worker = worker.split(' ')
        if int(worker[1]) < 20000:
            low.append(worker[0])
        total.append(worker[1])

    average = round(sum(map(int, total)) / len(total), 2)
    print(f'Сотрудники с з/п меньше 20.000 - {", ".join(low)}')
    print(f'Средняя зарплата по всем сотрудникам {average}')

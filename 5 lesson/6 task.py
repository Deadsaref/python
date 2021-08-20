with open('6_task.txt', 'r', encoding='utf-8') as f:
    subjects = {}
    for line in f:
        data = line.replace('(', ' ').split()
        subjects[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    print(subjects)

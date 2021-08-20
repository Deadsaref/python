from json import dump, load

with open('7_task.txt', 'r', encoding='utf-8') as f:
    firm_list = [{}, {}]
    lines = f.readlines()
    for line in lines:
        name, form, income, costs = line.split()
        earnings = int(income) - int(costs)
        firm_list[0][name] = earnings
    average_earnings = sum(total for name, total in firm_list[0].items() if total > 0) / len(lines)
    firm_list[1]['средняя прибыль'] = average_earnings
    print(firm_list)

with open('7_task.json', 'w', encoding='utf-8') as j:
    dump(firm_list, j)

# проверка десериализации

with open('7_task.json', 'r', encoding='utf-8') as jr:
    firm_list = load(jr)
    print(f'\nПосле десериализации\n{firm_list}')
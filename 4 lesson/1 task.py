from sys import argv


def my_func():
    time = int(argv[1])
    hourly_pay = int(argv[2])
    award = int(argv[3])
    salary = time * hourly_pay + award
    print(f'Заработная плата сотрудника - {salary}')


my_func()

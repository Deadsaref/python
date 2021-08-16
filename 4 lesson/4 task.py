old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def my_func(list):
    new_list = (el for el in list if list.count(el) == 1)
    for i in new_list:
        print(i)


my_func(old_list)

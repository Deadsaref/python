numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
bigger = [i for i in numbers if (i > numbers[numbers.index(i)-1] and i != numbers[0])]

print(bigger)
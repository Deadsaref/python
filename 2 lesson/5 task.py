rating = [8, 7, 3, 3, 2, 1]

new_number = int(input('Введите число: '))
rating.append(new_number)

print(sorted(rating, reverse=True))
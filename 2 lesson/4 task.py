message = input('Введите слова через пробел: ')

message = message.split(' ')
for id, word in enumerate(message, 1) :
    if len(word) <= 10:
        print(id, word)
    else:
        print(id, word[0:11])
number = 23


while not (guess := input('Введите целое число: ')).isdecimal():
    if guess == 'stop':
        break
else:
    print("Наконец-то число!!!")
    print('Поздравляю, вы угадали' if int(guess) == number else 'Не угадали')

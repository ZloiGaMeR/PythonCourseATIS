MINIMUM = 0
MAXIMUM = 100

def guess_number():
    number = 64
    while (guess := input(f"Введите целое число от {MINIMUM} до {MAXIMUM}: ")).isdigit():
        if number < int(guess):
            print(f"Загаданное число меньше {guess}")
        elif number > int(guess):
            print(f"Загаданное число больше {guess}")
        else:
            print(f"Вы угадали! Искомое число - {guess}")
            break
    return None


guess_number()





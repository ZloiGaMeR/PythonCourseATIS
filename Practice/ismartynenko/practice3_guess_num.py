import random

range = input("Input range (ex. 1-20):")
dim = range.split("-")
number = random.randint(int(dim[0]), int(dim[1]))
# print(number)
attempt = input("Input a number: ")
while attempt.isdigit() is True:
    if int(attempt) > number:
        print("Ваше число больше заданного. Попробуйте еще.")
    elif int(attempt) < number:
        print("Ваше число меньше заданного. Попробуйте еще.")
    else:
        print(f"Вы угадали, это число {number}")
        exit()
    attempt = input("Input a new number: ")
else:
    print("Указан нечисловой символ. Выход из приложения")

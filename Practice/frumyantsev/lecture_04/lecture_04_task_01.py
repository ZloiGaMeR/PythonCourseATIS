def fizz_buzz_func():
    """
    Выводит на экран числа от 1 до 100. Вместо чисел, кратных трем,
    выводит Fizz, вместо чисел, кратных пяти — Buzz.
    Если число кратно пятнадцати, то выводит слово FizzBuzz.
    """
    while (number := input("Введите число от одного до ста: ")).isdigit() and (int(number) in range(1, 101)):
        if int(number) % 15 == 0:
            print("FizzBuzz")
        elif int(number) % 3 == 0:
            print("Fizz")
        elif int(number) % 5 == 0:
            print("Buzz")
        else:
            print(number)
    return None


if __name__ == "__main__":
    fizz_buzz_func()

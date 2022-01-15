def string_slicer(func):
    """
    Выводит в новой строке каждый символ полученной строки.
    """

    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        for item in range(len(a)):
            print(f"{item+1} цифра равна {a[item]}")
        return a

    return wrapper


@string_slicer
def get_five_digit_number():
    """
    Cчитывает введённое пятизначное число.
    """
    while not ((some_string := input("Введите пятизначное число: ")).isdigit() and len(some_string) == 5):
        pass
    print(f"Считано число: {some_string}")
    return some_string


if __name__ == "__main__":
    get_five_digit_number()

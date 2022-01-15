def string_slicer(func):
    """
    Выводит в новой строке каждый символ полученной строки.
    """

    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        five_digit_number = [(i+1, a[i]) for i in range(len(a))]
        for item in five_digit_number:
            print(f"{item[0]} цифра равна {item[1]}")
        return None

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

def number_slicer():
    """
    Считывает введённое пятизначное число.
    После чего, каждую цифру этого числа выводит в новой строке
    """
    while not ((some_string := input("Введите пятизначное число: ")).isdigit() and len(some_string) == 5):
        pass
    else:
        five_digit_number = [(i+1, some_string[i]) for i in range(len(some_string))]
        for item in five_digit_number:
            print(f"{item[0]} цифра равна {item[1]}")
    return None


if __name__ == "__main__":
    number_slicer()

def number_slicer():
    """
    Считывает введённое пятизначное число.
    После чего, каждую цифру этого числа выводит в новой строке
    """
    while not ((some_string := input("Введите пятизначное число: ")).isdigit() and len(some_string) == 5):
        pass
    else:
        for i in range(len(some_string)):
            print(f"{i+1} цифра равна {some_string[i]}")
    return None


if __name__ == "__main__":
    number_slicer()

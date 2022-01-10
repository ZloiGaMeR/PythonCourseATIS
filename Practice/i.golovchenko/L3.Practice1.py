while 1:
    x = input("Введите число: ")
    if x.isdigit():
        print(x)
    elif x.lower() in "stop":
        print(x)
        break
    else:
        print(f"Введен не числовой символ: {x}")
        continue
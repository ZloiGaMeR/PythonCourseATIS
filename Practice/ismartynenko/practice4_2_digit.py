while len(digit := input("Введите 5-ти значное число: ")) != 5:
    continue
else:
    print("Число:", digit)
    for i, value in enumerate(digit, 1):
        print(f'{i} цифра равна {value}')

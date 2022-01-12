digit = input("Введите 5-ти значное число: ")
print("Число:", digit)
while len(digit) != 5:
    digit = input("Введите 5-ти значное число: ")
else:
    for i, value in enumerate(digit, 1):
        print(f'{i} цифра равна {value}')

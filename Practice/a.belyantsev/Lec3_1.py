number = ""
temp = ""
while 1:
    temp = input("Введите символ: ")
    if temp.lower() == "stop":
        break
    if temp.isdecimal():
        number += temp
    else:
        print("Введеный символ не является цифрой")


print(f"Получившееся число: {number}")

stroka = input("Input a number: ")
stroka_l = stroka.lower()
number = ' '
stopkey = "stop"

while stroka_l.find(stopkey) == -1:
    if stroka_l.isdigit():
        number += stroka_l
    else:
        print("You are input not a number, try again")
    stroka = input("Input a number: ")
    stroka_l = stroka.lower()

num = number.lstrip()
print(num)

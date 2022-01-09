str = input("Input a number: ")
number = ' '

while str.find("STOP") == -1:
    if str.isdigit():
        number += str
    else:
        print("You are input not a number, try again")
    str = input("Input a number: ")

num = int(number.lstrip())
print(num)

# max_value = lambda x = input("Key in value1: "), y = input("Key in value2: "): print(max(x,y))
#
# max_value()

def max_value(num1, num2):
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("Числа равны")
    return None


max_value(5, 12)
max_value(23, -3)
max_value(10, 10)

# max_value = lambda x = input("Key in value1: "), y = input("Key in value2: "): max(x,y)
#
# max_value_returned = max_value()
# print(f"Function \"max_value\" returns: {max_value_returned}") # проверка

def max_value(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return None


returned_result_1 = max_value(15, 12)
returned_result_2 = max_value(-23, -3)
returned_result_3 = max_value(-1, -1)
print(returned_result_1)
print(returned_result_2)
print(returned_result_3)
#
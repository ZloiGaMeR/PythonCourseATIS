def which_more_print(a, b):
    if a > b:
        print(f"{a} more than {b}")
    else:
        print(f"{b} more than {a}")


def which_more_return(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Input the first number: "))
b = int(input("Input the second number: "))
which_more_print(a, b)
# print(which_more_return(a, b))

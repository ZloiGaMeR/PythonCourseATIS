for i in range(1, 31):
    cond1 = i % 3 <= 0
    cond2 = i % 5 <= 0
    if cond1 and cond2 is True:
        print("FizzBuzz")
    elif cond1 is True:
        print("Fizz")
    elif cond2 is True:
        print("Buzz")
    else:
        print(i)

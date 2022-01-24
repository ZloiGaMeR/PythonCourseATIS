for i in range(1, 31):
    cond1 = i % 3 == 0
    cond2 = i % 5 == 0
    if cond1 and cond2:
        print("FizzBuzz")
    elif cond1:
        print("Fizz")
    elif cond2:
        print("Buzz")
    else:
        print(i)

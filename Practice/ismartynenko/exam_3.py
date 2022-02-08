def my_range(*args):
    i = 0
    lst = []
    ln = len(args)
    start = 0
    stop = args[0]
    step = 1

    if 1 <= ln <= 3 and args[2] != 0:
        if ln == 2:
            start = args[0]
            stop = args[1]
        elif ln == 3:
            start = args[0]
            stop = args[1]
            step = args[2]
    else:
        print("Problem with arguments. Exit")
        exit()

    if step > 0:
        while (cond := start + i * step) < stop:
            i += 1
            lst.append(cond)
    else:
        while (cond := start + i * step) > stop:
            i += 1
            lst.append(cond)
    return lst


res = my_range(10, 20, 1)
res2 = my_range(20, 10, -1)
res3 = my_range(-20, -10, 1)
print(res, res2, res3)

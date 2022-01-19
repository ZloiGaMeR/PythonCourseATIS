def mymax(arguments):
    """
    Принимает любое количество аргументов и возвращает максимальный аргумент:
    """
    max_val = float("-inf")
    for i in arguments:
        if i > max_val:
            max_val = i
    print(max_val)
    # for i in range(len(arguments)):
    #     if arguments[i] > max_val:
    #         max_val = arguments[i]
    # print(max_val)
    return max_val


if __name__ == "__main__":
    mymax([10, 27, 42, 36])
    mymax((3, 7, -1, -8, 0))
    mymax({-5, 8, 0, -6, 12, 3})

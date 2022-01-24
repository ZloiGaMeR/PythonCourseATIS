def my_enumerate(a):
    """
    Создает объект, который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента:
    # >>> a = [10, 20, 30, 40]
    # >>> for i in enumerate(a):
    # ... print(i)
    # ...
    # (0, 10)
    # (1, 20)
    # (2, 30)
    # (3, 40
    """

    lst = []
    for i in range(len(a)):
        lst.append((i, a[i]))
    for j in lst:
        print(j)


if __name__ == "__main__":
    my_enumerate([10, 20, 30, 40])

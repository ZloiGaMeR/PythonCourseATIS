import itertools


def func1(*args):
    return list(itertools.chain(*args))


def func2(lst):
    return list(itertools.takewhile(lambda x: len(x) > 4, sorted(lst, key=lambda l: len(l), reverse=True)))


def func3(word, length):
    return list(itertools.combinations(word, length))


if __name__ == "__main__":
    print(func1([1, 2, 3], [4, 5], [6, 7]))
    print(func2(['hello', 'i', 'write', 'cool', 'code']))
    print(func3('password', 4))



# fun1 = itertools.chain([1, 2, 3], [4, 5], [6, 7])
# print(list(fun1))

# fun2 = itertools.takewhile(lambda x: len(x) > 4, sorted(['hello', 'i', 'write', 'cool', 'code'],
#                                                         key=lambda l: len(l), reverse=True))
# print(list(fun2))

# fun3 = itertools.combinations('password', 4)
# print(list(fun3))

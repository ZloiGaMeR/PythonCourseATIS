# Функции на вход подаётся последовательность чисел source и множитель m.
# На выходе функции ожидается новая последовательность на основе source, где каждый член был умножен на m.
# Если source не был указан, то берётся последовательность[1, 2, 3].Укажите ошибки, допущенные в данной функции,
# и предложите свою реализацию
# def multiplier(m=1, source=[1, 2, 3]):
#     result = source
#     for i, x in enumerate(source):
#         result[i] *= m
#     return result
#
# >> > multiplier(5)
# [5, 10, 15]
# >> > multiplier(12, [1, 2])
# [12, 24]


def multiplier(m=1, source=(1, 2, 3)):
    return [x * m for x in source]


print(multiplier(5))
print(multiplier(12, [1, 2, 3, 4, 5]))
print(multiplier(3))
print(multiplier(3))


def multiplierold(m=1, source=[1, 2, 3]):
    result = source # result и source указывают на одну и ту же область памяти, в следствии чего при изменении result меняется и source
    print(result is source)
    for i, x in enumerate(source):
        result[i] *= m
    return result


print(multiplierold(3))
print(multiplierold(3))

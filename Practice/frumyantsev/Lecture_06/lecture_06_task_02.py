# def multiplier(m=1, source=[1, 2, 3]):
# использование изменяемого типа в качестве значения по умолчанию именованной переменной приводит к изменению данных по
# адресу данной переменной после очередного вызова функции без передачи значения в эту переменную
def multiplier(m=1, source=(1, 2, 3)):
    # result = [i*m for i in source]
    # result = list(source)
    # # for i, x in enumerate(source):
    # for i, x in enumerate(result):
    #     result[i] *= m
    # return result
    return [i*m for i in source]


print(multiplier(5))
print(multiplier(5))
print(multiplier(3, (3, 5, 7)))

# [5, 10, 15]
# >>> multiplier(12, [1,2])
# # [12, 24]
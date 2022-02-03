def multiplier(m=1, source=[1, 2, 3]):
    result = [i * m for i in source]
    return result


print(multiplier(5))
print(multiplier(12, [1, 2]))
lst = [1, 2]
print(multiplier(12, lst))
print(multiplier(12, lst))

def multiplier(m, source=None):
    if source is None:
        source = [1, 2, 3]
    result = list(source)
    for i, x in enumerate(source):
        result[i] *= m
    return result


lst = [1, 2]
print(multiplier(12, lst))
print(multiplier(12, lst))

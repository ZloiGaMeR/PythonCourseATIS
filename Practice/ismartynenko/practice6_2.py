def multiplier(m, source=None):
    if source is None:
        source = [1, 2, 3]
    result = source
    for i, x in enumerate(source):
        result[i] *= m
    return result


print(multiplier(5))
print(multiplier(12, [1, 2]))

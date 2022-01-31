def comparison(a, b):
    '''
    Функция принимает 2 числа и возвращает большее.
    a - первое число
    b - второе число
    '''
    if a > b:
        temp = a
    else:
        temp = b
    return temp


print(f"Большее число: {comparison(9, 99)}")

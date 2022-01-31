# Есть список списков (матрица). Каждый внутренний список - это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
def matrix_remover(number, matrix):
    for i in matrix:
        count = 0
        while count < len(i):
            if i[count] == number:
                for k in matrix:
                    k.pop(count)
            else:
                count += 1
    return matrix


listoflists = [
    [2, 3, 4, 2],
    [6, 3, 1, 3],
    [1, 3, 5, 5]
]
value = 2
print(listoflists)
print(matrix_remover(value, listoflists))

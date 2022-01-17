# Есть список списков (матрица). Каждый внутренний список - это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
def matrix_remover(number, matrix):
    for i in matrix:
        for j in i:
            if j == number:
                ind = (i.index(j))
                for k in matrix:
                    k.pop(ind)
                break
    return matrix


listoflists = [
    [2, 3, 4, 5],
    [6, 3, 6, 8],
    [1, 9, 7, 5]
]
value = 2
print(listoflists)
print(matrix_remover(value, listoflists))

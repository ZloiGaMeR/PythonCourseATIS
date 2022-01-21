# Есть список списков (матрица). Каждый внутренний список - это строка матрицы.
# Необходимо реализовать функцию, которая удаляет столбец, который содержит заданную цифру.
def matrix_remover(number, matrix):
    for i in matrix:
        print(f"{i=}")
        count = 0
        while count in range(len(i)):
            print(f"{i[count]}")
            if i[count] == number:
                for k in matrix:
                    print(k.pop(count))
                count = 0
            count += 1
    return matrix


listoflists = [
    [2, 3, 7, 2],
    [6, 3, 2, 3],
    [1, 9, 5, 5]
]
value = 2
print(listoflists)
print(matrix_remover(value, listoflists))

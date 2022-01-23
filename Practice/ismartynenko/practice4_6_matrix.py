matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15]]

delete_num = 8
delete_index = None

for j in matrix:
    for i in range(len(j)):
        if j[i] == delete_num:
            delete_index = i

for k, v in enumerate(matrix):
    del v[delete_index]

print(matrix)

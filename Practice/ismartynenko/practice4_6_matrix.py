matrix = [[1, 2, 3, 4, 8],
          [6, 7, 8, 9, 10],
          [8, 12, 13, 14, 15]]

delete_num = 8
delete_index = []

for j in matrix:
    for i in range(len(j)):
        if j[i] == delete_num:
            delete_index.append(i)

delete_index.sort(reverse=True)

for k in matrix:
    for v in delete_index:
        del k[v]

print(matrix)

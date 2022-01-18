arr = [0, 3, 24, 2, 3, 7]
for i in range(len(arr)-1):
    mini = min(arr[i:])
    mini_index = arr.index(mini, i)
    arr.insert(i, arr.pop(mini_index))

print(arr)

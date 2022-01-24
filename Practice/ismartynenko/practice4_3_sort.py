def minimal(a):
    mini = a[0]
    ind = 0
    for i in range(len(a)):
        if mini > a[i]:
            mini = a[i]
            ind = i
    return ind


arr = [0, 3, 24, 2, 3, 7]
arr2_sorted = []
while len(arr) != 0:
    arr2_sorted.append(arr.pop(minimal(arr)))

print(arr2_sorted)

# Razminka 1
def maximum(a):
    more = a[0]
    for i in a:
        if more < i:
            more = i
    return more


a = [10, 27, 42, 36]
max_value = maximum(a)
print(max_value)


# Razminka 2
a = [10, 20, 30, 40]
for i in range(len(a)):
    print(f"({i}, {a[i]})")

import random


def name_generator(num):
    s1 = "аеиоуэюя"
    s2 = "бвгджзклмнпрстфхчшщ"
    res = ""
    s = s2
    while len(res) < num:
        res += random.choice(s)
        s = s1 if s == s2 else s2
    return res


print(name_generator(4))
print(name_generator(5))
print(name_generator(6))
print(name_generator(7))



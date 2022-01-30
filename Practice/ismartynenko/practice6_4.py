import itertools


s = ([1, 2, 3], [4, 5], [6, 7])
s_new = itertools.chain.from_iterable(s)
print(list(s_new))

s1 = (['hello', 'i', 'write', 'cool', 'code'])
s1_new = itertools.filterfalse(lambda x: len(x) < 5, s1)
print(list(s1_new))

s2 = 'password'
s2_new = itertools.combinations(s2, 4)
print(list(s2_new))

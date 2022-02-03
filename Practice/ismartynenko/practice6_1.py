def chargen(n):
    i = 0
    while i < n:
        for c in '0123456789':
            yield c
            i += 1


words = (c + c for c in chargen(10))

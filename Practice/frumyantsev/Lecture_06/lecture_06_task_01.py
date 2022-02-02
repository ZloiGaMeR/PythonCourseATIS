def chargen():
    # while True: # ошибка бесконечный цикл без реализации выхода из цикла
    for c in '0123456789':
        yield c
words = [c + c for c in chargen()][:10]
print(words)

def palindrome(a):
    if a == a[::-1]:
        return a[::-1]
    else:
        print(f"Введеное слово: {a} - не палидром")

word = str(input("Введите слово: "))
print(palindrome(word))
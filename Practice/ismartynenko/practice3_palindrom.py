def check(word):
    backword = word[::-1]
    if word.find(backword) != -1:
        print("Palindrom")
    else:
        print("Not the palindrom")
    return None


word = input("Input word: ")
check(word)

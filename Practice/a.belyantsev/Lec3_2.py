def palindrome(word):
    word = word.lower()
    if word == word[::-1]:
        return True
    return False


print(palindrome("Ололо"))
print(palindrome("Топот"))
print(palindrome("Довод"))

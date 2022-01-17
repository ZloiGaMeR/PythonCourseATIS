def palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    return False


print(palindrome("Ололо"))
print(palindrome("Топот"))
print(palindrome("Довод"))

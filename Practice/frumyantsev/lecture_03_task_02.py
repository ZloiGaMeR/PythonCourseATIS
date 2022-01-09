def is_palindrome(s):
    """ (str) -> bool
    Check if keyed in string is palindrome. Return True or False
    """
    return True if str(s) == str(s[::-1]) else False


print(is_palindrome("1"))
print(is_palindrome("44"))
print(is_palindrome("1234"))
print(is_palindrome("3456543"))
print(is_palindrome("abracadabra"))
print(is_palindrome("abracarba"))
print(is_palindrome("a b racar b a"))


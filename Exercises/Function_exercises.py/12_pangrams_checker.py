"""14. Write a Python function to check whether a string is a pangram or not.
"""

string_w = input("Please enter your string: ").lower()
def pangram_check(string_w):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabets:
        if letter not in string_w:
            return False
    else:
        return True

print(pangram_check(string_w))
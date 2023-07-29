"""12. Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""

string_word = input("Enter a word: ")

def palondrome_checker(string_word):
    reversed_word = ""
    s_l = len(string_word)
    for letter in string_word:
        reversed_word += (string_word[s_l - 1])
        s_l = s_l - 1
    if reversed_word == string_word:
        return True
    else:
        return False
print(palondrome_checker(string_word))

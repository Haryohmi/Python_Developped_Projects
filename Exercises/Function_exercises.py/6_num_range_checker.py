"""6. Write a Python function to check whether a number falls within a given range.
"""

def number_check(n):
    if n in range(50,100):
        print(f"{n} is in the range ")
    else:
        print(f"{n} is outside the range ")
number_check(100)
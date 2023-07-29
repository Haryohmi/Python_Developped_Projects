"""1. Write a Python function to find the maximum of three numbers."""
no_1 = int(input("Enter a first number: "))
no_2 = int(input("Enter a 2nd number: "))
no_3 = int(input("Enter a 3rd number: "))
all_no = [no_1, no_2, no_3]


def find_max_number():
    height_number = max(no_1, no_2, no_3)
    return height_number

#OR
def find_max_number():
    ns = 0
    for n in all_no:
        if n > ns:
            ns = n
    print(ns)

find_max_number()
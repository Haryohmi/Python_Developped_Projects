"""9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
"""

number = int(input("Please write a number: "))
def prime_checker(number):
    if number > 1:
        for n in range(2, number):
            if number % n == 0:
                return False
        else:
            return True
    else:
        return False

print(prime_checker(number))
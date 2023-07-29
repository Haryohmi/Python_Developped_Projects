"""5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument."""
n = int(input("Enter a non-negative integer"))
def factorial_no_calculator(n):
    sam = 1
    if n > 1:
        for num in range(1, n+1):
            new_sam =  sam * num
            sam = new_sam
        print(sam)
factorial_no_calculator(n)
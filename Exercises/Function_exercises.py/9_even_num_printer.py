"""10. Write a Python program to print the even numbers from a given list.
"""
sample_List = [1,2,3,4,5,6,7,8,9]
expected_result = []
for num in sample_List:
    if num % 2 == 0:
        expected_result.append(num)
print(expected_result)
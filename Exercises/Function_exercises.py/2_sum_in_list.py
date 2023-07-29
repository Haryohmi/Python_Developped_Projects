"""2. Write a Python function to sum all the numbers in a list.
"""
sample_List = 8,2,3,0,7

def sum_number_in_list():
    return sum(sample_List)
#OR

ns = 0
for n in sample_List:
    ns += n
print(ns)

print(sum_number_in_list())
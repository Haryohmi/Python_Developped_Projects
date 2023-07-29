"""3. Write a Python function to multiply all the numbers in a list.
"""
sample_List = 8,2,3,-1,7

def multiplying_funtion():
    ns = 1
    for n in sample_List:
        ns *= n
    return ns

print(multiplying_funtion())
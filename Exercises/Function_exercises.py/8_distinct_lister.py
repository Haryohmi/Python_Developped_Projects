"""8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
"""
def lister():
    sample_list = [1,2,3,3,3,3,4,5]
    unique_list = []
    for x in sample_list:
        if x not in unique_list:
            unique_list.append(x)
        return x
    print(unique_list)


print(lister())

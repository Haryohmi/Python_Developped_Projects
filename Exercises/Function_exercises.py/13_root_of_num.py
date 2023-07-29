"""16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
"""
def v_list():
    d_list = []
    for n in range(1,31):
        num = n ** 2
        d_list.append(num)
    print(d_list)

v_list()
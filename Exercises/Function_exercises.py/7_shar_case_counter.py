"""7. Write a Python function that accepts a string and counts the number of upper and lower case letters."""
n = "The quick Brow Fox"

def string_counter(n):
    low_case1 = []
    up_case2 = []
    ln = len(n)
    for x in range(ln):
        st = n[x]
        if st.islower() is True:
            low_case1.append(st)
        else:
            up_case2.append(st)
    low_case1 = len(low_case1)
    up_case2 = len(up_case2)

    print(f"No of Lower case characters: {low_case1}")
    print(f"No of Upper case characters: {up_case2}")

string_counter(n)

##################################

def string_counter(n):
    dic = {
        "low_case": 0,
        "up_case": 0
    }

    for x in (n):
        if x.islower():
            dic["low_case"]+= 1
        elif x.isupper():
            dic["up_case"]+= 1
    

    print("No of Lower case characters: ", dic["low_case"])
    print("No of Upper case characters: ", dic["up_case"])


string_counter(n)

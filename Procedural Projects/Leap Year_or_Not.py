year = int(input("Which year do you want to check? "))
print("Welcome to Leap Year checker Machine")
if year % 4 == 0:
    #print("Leap Year.")
    if year % 100 == 0:
        #print(" Not a Leap Year.")
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year")



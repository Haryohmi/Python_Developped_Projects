print("Welcome to ticket checking Machine")
height = int(input("What is your height? "))
bill = 0
if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age >= 45 and age <= 55:
        bill = 0
        print(f"You'll pay ${bill}.")
    elif age < 12:
        bill += 5
        #print("You'll pay $5")
    elif age <= 18:
        bill += 7
        #print("You'll pay $7")
    else:
        #print("You'll pay $12")
        bill += 12
    photo = input("Would you like photo? Y or N ")
    if photo == "Y":
        bill += 3
        print(f"You'll pay ${bill}")
else:
    print("Sorry, You can't ride.")


print("Welcome to ticket checking Machine")
height = int(input("What is your height? "))
if height >= 120:
    print("You can ride.")
    age = int(input("What is your age? "))
    if age < 12:
        print("You'll pay $5")
    elif age >= 12 & age <= 18:
        print("You'll pay $7")
    else:
        print("You'll pay $12")
else:
    print("Sorry, You can't ride.")


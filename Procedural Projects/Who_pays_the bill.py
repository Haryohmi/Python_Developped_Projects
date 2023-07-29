# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random
no_of_names = len(names)
choice = random.randint(0,no_of_names)
person = names[choice]
print(person + " is going to buy the meal today!")
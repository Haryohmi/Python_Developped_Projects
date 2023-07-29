#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

number = random.randint(0,1)
if number == 0:
    print("Tails")
else:
    print("Heads")

#for dice
import random
number = random.randint(1,6)
print(f"You lucky number is {number}, try again.")
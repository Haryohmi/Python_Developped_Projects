# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# nr_letters = nr_letters +1
# nr_symbols = nr_numbers +1
# nr_numbers = nr_numbers +1
password = ""
password1 = ""
password2 = ""

for num_l in range(nr_letters):
    password += random.choice(letters)
    #or use password.append(random.choice(letters)))
#print(password)
    
for num_s in range(nr_symbols):
    password1 += random.choice(symbols)
    #or use password1.append(random.choice(symbols)))
#print(password1)
    
for num_n in range(nr_numbers):
    password2 += random.choice(numbers)
    #or use password2.append(random.choice(numbers)))
#print(password2)
    
print(f"Here is your password: {password}{password1}{password2}")

passwords = password + password1 + password2

harder_password = ""
for result_password in (passwords):
    harder_password += random.choice(passwords)
    #or use harder_password.append(random.choice(passwords))
print(f"Here is your password:{harder_password}")

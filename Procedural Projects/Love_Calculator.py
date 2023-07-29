print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
#print(names)
names = names.lower()
#print(names)
T_N = names.count("t")
R_N = names.count("r")
U_N = names.count("u")
E_N = names.count("e")
True_count = int(T_N + R_N + U_N + E_N)
#print(True_count)
L_N = names.count("l")
O_N = names.count("o")
V_N = names.count("v")
E_N = names.count("e")
Love_count = int(L_N + O_N + V_N + E_N)
Total = str(True_count) + str(Love_count)
#print(Total)
Total = int(Total)
if Total < 10 or Total > 90:
    print(f"Your score is {Total}, you go together like coke and mentos.")
elif Total >= 40 and Total <= 50:
    print(f"Your score is {Total}, you are alright together.")
else:
    print(f"Your score is {Total}.")




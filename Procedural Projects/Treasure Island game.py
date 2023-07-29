print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


step_1 = input("What turning do you want to take? left or right \n").lower()
if step_1 == "right":
    step_2 = input("You got to the river, do you want to swim or wait for boat? swim or wait \n").lower()
    if step_2 == "wait":
        step_3 = input("You arrived the island, which door will you enter? red or blue or yellow \n").lower()
        if step_3 == "red":
            print("Fire!!!, You are dead!")
        elif step_3 == "blue":
            print("Congratulations, you saw the treasure!")
        else:
            print("Gosh Pithole !, You are dead!!")
    else:
        print("Sorry, You got eaten by Shake")
else:
    print("Sorry, you fell into a pit, Game over.")
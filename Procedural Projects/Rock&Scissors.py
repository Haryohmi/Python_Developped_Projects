rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
# Rock wins against scissors. 
# Scissors win against paper. 
# Paper wins against rock.    
import random

player = int(input("what do you choose? 0 for rock, 1 for paper or 2 for scissors?\n "))
computer1 = random.randint(0,2)


game_image = [rock, paper, scissors]


print(f"You chose {player}")
if player >= 0 and player <=3:
  print(game_image[player])
  print(f"Computer chose {computer1}.")
  print(game_image[computer1])


  if computer1 == 0 and player == 2:
    print("You lose !")
  elif player == 0 and computer1 == 2:
    print("You won")
  elif player == computer1:
    print("Draw")
  elif player > computer1:
    print("You won")
  elif computer1 > player:
    print("You lose !")
else:
  print("You lose by entering invalid figure. Please, enter 0 for rock, 1 for paper or 2 for scissors ")


  
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# from Art import logo
import random

# def check_guess_number():
#   user_guess = int(input("Make a guess "))
#   if user_guess > computer_guess:
#     result = "Too high\nGuess again\nYou have {level} remaining to guess the number"
#   elif user_guess < computer_guess:
#     result = "Too low\nGuess again\nYou have {level} remaining to guess the number"
#   else:
#     user_guess == computer_guess
#     result = f"You got it, the number was {computer_guess}"
#     return result

# print(logo)
print("Welcome to number guessing game")
print("I'm thinking of a number between 1 and 100, can you guess the number?")
computer_guess = random.choice(range(1, 100))

let_play = False
while let_play == False:
    level = input("choose difficulty level easy or hard? ").lower()
    if level != "easy" and level != "hard":
        print("Wrong input,try again.")
    elif level == "easy":
        let_play = True
        level = 5
    elif level == "hard":
        let_play = True
        level = 10

print(f"You have {level} attempts to your guess")

continue_game = False
while continue_game == False:
    if level > 0:
        level -= 1
        user_guess = int(input("Make a guess "))
        if level <= 0:
            print("You're out of guess, try again.")
        elif user_guess > computer_guess:
            print(
                f"Too high\nGuess again\nYou have {level} remaining to guess the number."
            )
        elif user_guess < computer_guess:
            print(
                f"Too low\nGuess again\nYou have {level} remaining to guess the number."
            )
        elif user_guess == computer_guess:
            continue_game = True
            print(f"You got it, the number was {computer_guess}.")

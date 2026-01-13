import random

from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
a = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

b = int(random.randint(1,100))
print(b)

if a == "easy":
    number_chances = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    number_chances = 5
    print("You have 5 attempts remaining to guess the number.")

for i in range(number_chances):
    user_choice = int(input("Make a guess: "))

    if user_choice == b:
        print("You guessed the right number!")
        print(f"{b} was the number!")
        break

    elif user_choice > b:
        print("Too high!")
        print("Guess again!")
        number_chances -= 1
        print(f"You have {number_chances} attempts remaining to guess the number.")
        if number_chances == 0:
            print("You have run out of guesses, you lose!")
    else:
        print("Too low!")
        print("Guess again!")
        number_chances -= 1
        print(f"You have {number_chances} attempts remaining to guess the number.")
        if number_chances == 0:
            print("You have run out of guesses, you lose!")



"""
Implement a guessing game where the computer generates a random number 
between 1 and 100, and the user has to guess the number.


"""

import random

def guessing_game():

    secret_number = random.randint(1, 100)
    
    print("Welcome to the Guessing Game!")
    print("I've picked a random number between 1 and 100. Can you guess it?")
    
    attempts = 0
    while True:
        guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break


guessing_game()

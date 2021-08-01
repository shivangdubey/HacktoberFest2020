# Imports.
import random

# Welcome message.
print("Welcome to the guessing game!")

# Get player's name.
name = input("What is your name?: ")

# Set minimum and maximum to None to allow us to perform a for loop.
minimum = None
maximum = None

# Ask the user to enter a minimum and a maximum number.
## One would think that it would be better to have both inputs in the same while loop however if the user
## gets the maximum number wrong they would have to renter the minimum number then do the maximum number again.
while minimum == None: 
    try:
        minimum = int(input("Please enter a minimum number: "))
    except ValueError:
        print("Please provide a numeric number!")
while maximum == None:
    try:
        maximum = int(input("Please enter a maximum number: "))
    except ValueError:
        print("Please provide a numeric number!")

    # If the minimum number is greater then the maximum ask the user to enter a new maximum.
    if maximum < minimum:
        print(f"Please provide a number greater than {minimum}!")
        maximum = None

# Generate the number by doing randint.
number = random.randint(minimum, maximum)

while True:

    # If the guess isn't a number ask them to provide a number.
    try:
        guess = int(input("Please provide a guess: "))
    except ValueError:
        print("Please provide a numeric number!")

    # If the guess is the number let them know, otherwise tell them if they're too high or too low.
    if guess == number:
        print(f"Nice job {name}, you guessed the right number!")
        break
    print("Too low!" if guess < number else "Too high!")

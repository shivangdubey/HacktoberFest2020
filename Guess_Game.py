import random
import math

# function definitions


def runGame(start, stop, guesses):
    answer = random.randint(start, stop)
    while guesses < 5:
        user_input = int(input("Guess Something : "))
        if user_input == answer:
            print("Hurray " + user_name + " You Have Done It.")
            break
        elif user_input > answer:
            print("Um! You Guessed Little High, try again!")
        elif user_input < answer:
            print("Oh! You guessed Bit Lower, Try again!")


# Welcome Message
print("Welcome to Guess Game")

# Getting Player Name and options to play

while True:
    # checking whether input is integer.
    user_name = input("Enter your Name : ")
    if user_name.isdigit():
        print("Please enter a valid name")
        continue

    else:
        break


# Getting Choices
print(user_name.upper() + " What Do You Wish To Guess? : ")
print("You have got Infinite Chances, Relax!")
print("Option A: 10-20", "Option B: 20-30",
      "Option C: 30-40", "Option D: 40-50", sep='\n')
choice_input = input("Enter your Choice : ")
# Setting Guess counter


def choicer(choice_input):
    guesses = 0

    # For User selecting option A
    if choice_input.lower() == "a":
        runGame(10, 21, guesses)
    # For User selecting option B
    if choice_input.lower() == "b":
        runGame(20, 31, guesses)

    # For User selecting option C
    if choice_input.lower() == "c":
        runGame(30, 41, guesses)

    # For User selecting option D
    if choice_input.lower() == "d":
        runGame(40, 51, guesses)

    else:
        print("Option A: 10-20", "Option B: 20-30",
              "Option C: 30-40", "Option D: 40-50", sep='\n')
        choice_input = input("Enter your Choice : ")
        choicer(choice_input)


choicer(choice_input)

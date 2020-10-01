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
#Welcome Message
print("Welcome to the Guess Game")

#Getting Player Name and options to play
user_name = input("Enter your name : ")

#Getting Choices
print(user_name + " enter the choice between which you wish to guess : ")
print("You have got infinite chances, chill and  all the best !")
print("Option A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50", sep = '\n')
#Setting Guess counter
def guess_number(user1):
    guesses = 0
    user1=user1.upper()
    if user1== "A":
        answer_user1 = random.randint(10, 21)
    elif user1== "B":
        answer_user1 = random.randint(20, 31)
    elif user1== "C":
        answer_user1 = random.randint(30, 41)
    elif user1== "D":
        answer_user1 = random.randint(40, 51)
    while guesses < 5:
        user_input = input("Enter your Guess : ")
        try:
            user_input=int(user_input)
            if user_input == answer_user1:
                print("Congratulations " + user_name + " you did it.")
                break
            elif user_input > answer_user1:
                print("Oh! You guessed higher, try again!")
            elif user_input < answer_user1:
                print("Oh! You guessed lower, try again!")
            guesses=guesses+1
            print(f"No of guesses left {5-guesses}")
        except ValueError:
            print("Pls Input Intergers only! TRY AGAIN")
            continue
    if guesses>=5:
        print("Game Over")

 debug-branch
#For User selecting option A
if choice_input.lower()=="a":
    runGame(10,21,guesses)
#For User selecting option B
if choice_input.lower()=="b":
    runGame(20,31,guesses)
 master

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
choice_input = input("Enter your Choice : ")
guess_number(choice_input)

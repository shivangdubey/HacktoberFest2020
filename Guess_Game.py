import random
import math

#function definitions

def runGame(start, stop):
    answer = random.randint(start, stop)
    while guesses < 5:
        user_input = int(input("Enter your Guess : "))
        if user_input == answer:
            print("Congratulations " + user_name + " you did it.")
            break
        elif user_input > answer:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer:
            print("Oh! You guessed lower, try again!")

#Welcome Message
print("Welcome to the Guess Game")

#Getting Player Name and options to play
user_name = input("Enter your name : ")

#Getting Choices
print(user_name + " enter the choice between which you wish to guess : ")
print("You have got infinite chances, chill and  all the best !")
print("Option A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50", sep = '\n')
choice_input = input("Enter your Choice : ")
#Setting Guess counter
guesses = 0

#For User selecting option A
if choice_input.lower()=="a:
    runGame(10,21)
#For User selecting option B
if choice_input.lower()=="b":
    runGame(20,31)

#For User selecting option C
if choice_input.lower()=="c":
    runGame(30,41)

#For User selecting option D
if choice_input.lower()== "d":
    runGame(40,51)


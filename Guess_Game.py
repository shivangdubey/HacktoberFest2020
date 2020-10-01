import random
import math
#Welcome Message
print("Welcome to the Guess Game")

#Getting Player Name and options to play
user_name = input("Enter your name")

#Getting Choices
print(user_name + " enter the choice between which you wish to guess")
print("You have got infinite chances, chill and  all the best !")
print("Option A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50", sep = '\n')
choice_input = input("Enter your Choice: ")

#Setting Guess counter
guesses = 0

#For User selecting option A
if choice_input == "A" or "a":
    answer_a = random.randint(10, 21)
    while guesses < 5:
        user_input = int(input("Enter your Guess"))
        if user_input == answer_a:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_a:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer_a:
            print("Oh! You guessed lower, try again!")

#For User selecting option B
if choice_input == "B" or "b":
    answer_b = random.randint(20, 31)
    while guesses < 5:
        user_input = int(input("Enter your Guess"))
        if user_input == answer_b:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_b:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer_b:
            print("Oh! You guessed lower, try again!")

#For User selecting option C
if choice_input == "C" or "c":
    answer_c = random.randint(30,  41)
    while guesses < 5:
        user_input = int(input("Enter your Guess"))
        if user_input == answer_c:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_c:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer_c:
            print("Oh! You guessed lower, try again!")

#For User selecting option D
if choice_input == "D" or "d":
    answer_d = random.randint(40, 51)
    while guesses < 5:
        user_input = int(input("Enter your Guess"))
        if user_input == answer_d:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_d:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer_d:
            print("Oh! You guessed lower, try again!")

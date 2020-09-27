import random
import math

print("Welcome to the Guess Game")

user_name = input("Enter your name")


print(user_name + " enter the choice between which you wish to guess")
print("You have got infinite chances, chill and  all the best !")
print("Option A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50", sep = '\n')
choice_input = input("Enter your Choice: ")


guesses = 0


if choice_input == "A" or "a":
    answer_a = random.randint(10, 21)
    while guesses < 5:
        user_input = (input("Enter your Guess")
        if user_input = answer_a:
            print("Congratulations " + user_name + " you did it")
            break
        else user_input > answer_a:
            print("Oh! You guessed higher, try again!")
        else user_input < answer_a:
            print("Oh! You guessed lower, try again!")


if choice_input == "B" or "b":
    answer_b = random.randint(20, 31)
    while guesses < 5:
        user_input = (input("Enter your Guess")
        if user_input = answer_b:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_b:
            print("Oh! You guessed higher, try again!")
        else user_input < answer_b:
            print("Oh! You guessed lower, try again!")


if choice_input == "C" or "c":
    answer_c = random.randint(30,  41)
    while guesses < 5:
        user_input = input("Enter your Guess")
        if user_input = answer_c:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer_c:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer_c:
            print("Oh! You guessed lower, try again!")


if choice_input == "D" or "d":
    answer_d = random.randint(40, 51)
    while guesses < 5:
        user_input = input("Enter your Guess")
        if user_input = answer_d:
            print("Congratulations " + user_name + " you did it")
            break
        else user_input > answer_d:
            print("Oh! You guessed higher, try again!")
        else user_input < answer_d:
            print("Oh! You guessed lower, try again!")

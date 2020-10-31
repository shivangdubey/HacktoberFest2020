import random
import math
#Welcome Message
print("Welcome to the Guess Game")

#Getting Player Name and options to play
user_name = input("Enter your name: ")

#Getting Choices
print(user_name + " enter the choice between which you wish to guess")
print("You have got infinite chances, chill and  all the best !")
print("\tOption A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50","Option E :Hard", sep = '\n\t')
choice_input = input("Enter your Choice: ")

#This funtion checks the 
def check(answer):
    while guesses < 5:
        user_input = int(input("Enter your Guess: "))
        if user_input == answer:
            print("Congratulations " + user_name + " you did it")
            break
        elif user_input > answer:
            print("Oh! You guessed higher, try again!")
        elif user_input < answer:
            print("Oh! You guessed lower, try again!")

#Setting Guess counter
guesses = 0

#For User selecting option A
if(choice_input == "A" or choice_input ==  "a"):
    answer = random.randint(10, 21)


#For User selecting option B
if (choice_input == "B" or choice_input == "b"):
    answer = random.randint(20, 31)
    

#For User selecting option C
if (choice_input == "C" or choice_input == "c"):
    answer = random.randint(30,  41)

#For User selecting option D
if (choice_input == "D" or choice_input ==  "d"):
    answer = random.randint(40, 51)
 
#For user selecting option E
if (choice_input == "E" or choice_input ==  "e"):
    answer = random.randint(1,10000)

#Calling the check function
check(answer)

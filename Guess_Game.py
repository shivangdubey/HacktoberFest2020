import random
import math
import colorama
#Welcome Message
colorama.init()

print(colorama.Fore.CYAN+"Welcome to the Guess Game",colorama.Style.RESET_ALL)

#Getting Player Name and options to play
user_name = input(colorama.Fore.GREEN+"Enter your name :"+colorama.Style.RESET_ALL)

#Getting Choices
print(colorama.Fore.YELLOW+user_name + " enter the choice between which you wish to guess : ")
print("You have got infinite chances, chill and  all the best !"+colorama.Style.RESET_ALL)
print(colorama.Back.CYAN+colorama.Fore.BLACK+"Option A: 10-20","Option B: 20-30", "Option C: 30-40", "Option D: 40-50",colorama.Style.RESET_ALL, sep = '\n')
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
        user_input = input(colorama.Fore.GREEN+"Enter your Guess : "+colorama.Style.RESET_ALL)
        try:
            user_input=int(user_input)
            if user_input == answer_user1:
                print(colorama.Fore.LIGHTMAGENTA_EX+"Congratulations " + user_name + " you did it."+colorama.Style.RESET_ALL)
                break
            elif user_input > answer_user1:
                print(colorama.Fore.LIGHTRED_EX+"Oh! You guessed higher, try again!"+colorama.Style.RESET_ALL)
            elif user_input < answer_user1:
                print(colorama.Fore.LIGHTRED_EX+"Oh! You guessed lower, try again!"+colorama.Style.RESET_ALL)
            guesses=guesses+1
            print(colorama.Fore.YELLOW+f"No of guesses left {5-guesses}"+colorama.Style.RESET_ALL)
        except ValueError:
            print(colorama.Fore.CYAN+"Pls Input Intergers only! TRY AGAIN"+colorama.Style.RESET_ALL)
            continue
    if guesses>=5:
        print(colorama.Back.BLUE+colorama.Fore.GREEN+"Game Over"+colorama.Style.RESET_ALL)


choice_input = input(colorama.Fore.GREEN+"Enter your Choice : "+colorama.Style.RESET_ALL)
guess_number(choice_input)



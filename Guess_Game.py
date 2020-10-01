print("WELCOME TO THE LUCKY NO GUESSING GAME")
import math
import random
print("think of a nop beetween 0-10")
n=int(input("Enter A No: "))
x=math.random(0,10)
print("RULES: PLAY NORMALLY AND WRITE 11 TO TERMINATE OR EXIT THE GAME")
while (n!=11):
    if (n==x):
        print("YOU ARE THE LUCKY WINNER")
    else:
        print("BETTER LUCK NEXT TIME")
print("THANKS FOR PLAYING OUR GAME")

import random
lis = ["S", "W", "G"]
print("Snake Water Game Starts")
i = 1
c = 1
c1 = 1
while i <= 10:
    user_input = input("Enter S, W, G ")
    choice = random.choice(lis)
    if ((choice == "S" and user_input == "W") or (choice == "W" and user_input == "G") or
            (choice == "G" and user_input == "S")):
        c = c+1
    elif ((choice == "S" and user_input == "G") or (choice == "W" and user_input == "S") or
            (choice == "G" and user_input == "W")):
        c1 = c1+1
    print(c, " ", c1)
    i = i+1

if c < c1:
    print("Wins")
elif c > c1:
    print("Loses")
else:
    print("Ties")

print("Game Over")

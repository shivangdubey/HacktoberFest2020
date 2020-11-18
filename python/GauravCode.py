x = 54
n = int(input("How many guesses you want?"))
i = 1
c = 0
while(i<=n):
    x1 = int(input("Enter number for guessing"))
    c = c+1
    i = i+1
    if(x1>x):
        print("Number entered should be less")
    elif(x>x1):
        print("Number entered should be more")
    else:
        print("Number found", "No of guesses left = ", n-c)
        print("Game Over")
        break

if(c==n):
    print("Guess are over" , "Number not found")

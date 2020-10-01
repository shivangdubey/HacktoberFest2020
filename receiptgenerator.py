sum =0;
while(True):
    userInput = input("Enter the item  price or press q to quit:\n")
    if(userInput!='q'):
        sum =sum + int(userInput)
        print(f"order total so far : {sum}")


    else:
        print(f" your total Bill is {sum}.Thanks for shopping with us")
        break

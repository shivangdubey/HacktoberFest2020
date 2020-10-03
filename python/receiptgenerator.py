# Initialise sum to zero.
sum = 0;
# Run an infinite loop and break when the user wishes to quit.
while(True):
    # Accept user input
    userInput,quantity = input("Enter the item  price and quantity or press q to quit:\n").split()
    # Calculate the bill if user input is not 'q', i.e. to quit the program.
    if(userInput != 'q'):
        # Calculate total amount and print the total amount calculated till now.
        sum = sum + (int(userInput)*int(quantity))
        print(f"order total so far : {sum}")
    else:
        # Print total amount and exit from the program.
        print(f" your total Bill is {sum}.Thanks for shopping with us")
        break

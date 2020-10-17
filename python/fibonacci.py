#I've included while loop and try except so that invalid inputs can be detected and error message printed
while True:
    num = input("Enter the Number:")
    try:
        n = int(num)
        break
    except:
        print("Invalid Input. You can enter only positive integers.")
n1, n2 = 0, 1
#In the following line there was a slight mistake, it was written end=','
#I replaced it with end=" " so that it remains consistent with line 17 of the code
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, n):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

#Here I have omitted print() because that was unnecessary.

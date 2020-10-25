'''
A given number x is an Armstrong number of order n if sum of 
digit of x each raised to the power n gives back x.

Note : This program can also be used to output the order of x
via the function order(x).

'''
def power(x,y):
    if y==0:
        return 1
    if y%2==0:
        return power(x,y//2) * power(x,y//2)
    return x*power(x, y//2)*power(x, y//2)

def order(x): #calculates order of the number
    n = 0
    while (x != 0):
        n = n+1
        x = x//10
    return n

def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    
    while(temp != 0):
        r = temp%10
        sum1 = sum1 + power(r,n)
        temp = temp // 10
        
    return (sum1 == x) #if the condition is satisfied

n = int(input())
isArmstrong(n)

#print(order(n))

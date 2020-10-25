def is_prime(a):
    flag = True
    for i in range(2,a//2+1):
        if(a%i == 0):
            flag = False
            break
    return flag
number = int(input('Enter a Number to which You want to find Prime Numbers : '))
if(number < 2):
    print('No Prime numbers < 2')
else:
    for i in range(2, number):
        if(is_prime(i)):
            print(i)
def is_prime(a):
    if type(a) != int:
        return False
    if a<2:
        return False
    if a==2:
        return True
    if a%2==0:
        return False
    for i in range(3,int(a**0.5)+1,2):
        if a%i==0:
            return False
    return True

number = int(input('Enter a Number to which You want to find Prime Numbers : '))

for i in range(2, number):
    if(is_prime(i)):
        print(i)

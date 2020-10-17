def simple_interest(p,t,r): 
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r) 
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si) 
    return si 
     
#Main Code
print("Input principal amount, rate of interest and time; seperated by new line")
p = input()
r = input()
t = input()

simple_interest(p,t,r)

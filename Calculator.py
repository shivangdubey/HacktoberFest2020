#Create Calculator Using The Simplest Method.
print("Welcome To Our Simple Calculator")
#Dfining sum function
import math
def sum(a,b):
    c=a+b
    return c
#Defining difference function
def sub(a,b):
    c=a-b
    return c
#Defining division function
def mul(a,b):
    c=a*b
    return c
#Defining multiplication function
def div(a,b):
    c=a/b
    return c
a=int(input("enter the first no."))
b=int(input("enter the second no."))
print(press 1 to add, press 2 to substract, press 3 to multiply, press 4 to divide, press 5 to get sin value, press6 to get cos value, press 7 to get tan value, press 8 to getpower value")
choice=int(input("enter your choice"))
if (choice==1):
      print(sum(a,b))
elif (choice==2):
      print(sub(a,b))
elif (choice==3):
      print(mul(a,b))
elif (choice==4):
      print(div(a,b))
elif (choice==5):
      print(math.sin(a))
elif (choice==6):
      print(math.cos(a,b))
elif (choice==7):
      print(math.tan(a))
elif (choice==8):
      print(math.pow(a,b))
else:
      print("value error")

# -*- coding: utf-8 -*-

# 1.	Alice and Bob agree on a prime number p and a base g
# 2.	Alice chooses a secret number a, and sends Bob (g^a mod p)
# 3.	Bob chooses a secret number b, and sends Bob (g^b mod p)
# 4.	Alice computes ((g^b mod p)^a mod p)
# 5.	Bob computes ((g^a mod p)^b mod p)
# 6.	Alice and Bob can use this number as key

from sympy import isprime 

while(True):
    prime_p = int(input("Enter a prime number P: "))
    base_g = int(input("Enter a base number G: "))
    if (isprime(prime_p) and isprime(base_g)):
        break
    else:
        print("Enter prime numbers only.")
    
a = int(input("Alice secret key: "))  # alice secret 
b = int(input("Bob secret key: ")) # bob secret


def alice(prime_p, base_g, a,b):
    a_send = ((pow(base_g , a)) % prime_p )
    bob_computes(a_send,b,prime_p)

def bob(prime_p, base_g, a ,b):
    b_send = ( (pow(base_g , b)) % prime_p )
    alice_computes(b_send,a,prime_p)
   
    
   
def alice_computes(bob,a,prime_p):
    bob_message = (pow(bob,a) % prime_p)
    print("Bob's Shared Key = {}".format(bob_message))
    
def bob_computes(alice,b,prime_p):
    alice_message = (pow(alice,b) % prime_p)
    print("\nAlice's Shared Key = {}".format(alice_message))
 
S = alice(prime_p, base_g, a,b)
A = bob(prime_p, base_g, a ,b)
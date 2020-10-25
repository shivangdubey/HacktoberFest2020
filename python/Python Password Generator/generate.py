import string
from random import *
char = string.ascii_letters + string.punctuation + string.digits 
passwordGenerator = "".join(choice(char) for x in range(randint(8,16)))
print(passwordGenerator)
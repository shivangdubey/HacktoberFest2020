import random 
a=[]
b=[]
c=[]
for j in range (65,91):
    a.append(chr(j))
for k in range (97,122):
    b.append(chr(k))
for i in range (90,97):
    c.append(chr(i))
d=range(0,10)
password=(random.choice(a))+(random.choice(b))+(random.choice(c))+str(random.choice(d))+(random.choice(a))+(random.choice(b))+(random.choice(c))+str(random.choice(d))
print(password)

# -*- coding: utf-8 -*-
#Use a Python 3.7

# %%
price = [524_000,527_000,520_000,534_000,526_000,538_000,544_000,530_000,550_000,559_000]

sale = [530_000,535_000,523_000,541_000,528_000,543_000,553_000,538_000,567_000,571_000]


# %%
sigmaX, sigmaY, sigmaX2, sigmaY2, sigmaXY = 0, 0, 0, 0, 0

n = len(price)

for i in range(len(price)):
   sigmaX   += price[i]
   sigmaY   += sale[i]
   sigmaX2  += price[i]**2
   sigmaY2  += sale[i]**2
   sigmaXY  += price[i] * sale[i]

print("*"*30)
print(sigmaX, sigmaY, sigmaX2, sigmaY2, sigmaXY, sep="\n")
print("*"*30)

# %%
a_num   = (sigmaY * sigmaX2) - (sigmaX * sigmaXY)
a_denum = n * sigmaX2 - sigmaX**2

alpha = a_num / a_denum

b_num   = n * sigmaXY - sigmaX * sigmaY
b_denum = n * sigmaX2 - sigmaX**2

beta = b_num / b_denum

print(alpha, beta, sep="\n")
# %%
print("\nSimple Linier Regression:")
print("Y = ",alpha," + ",beta,"X", sep="")

def f(x):
    return alpha + beta*x
print("What if = 5720000 ")
print("And we sale : ", f(572_000))

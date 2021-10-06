def MatrixPrint(X):
    for i in X:
        print(i)

def MatrixInput(a,b):
    X=[]
    for i in range(a):
        temp=[]
        for j in range(b):
            print("Enter Element of Row",i+1,"and Column",j+1,": ",end="")
            temp.append(float(input()))
        X.append(temp)
    return X
    
print('FIRST MATRIX')
m=int(input("Enter Number of Rows    : "))
n=int(input("Enter Number of Columns : "))
A=MatrixInput(m,n)
MatrixPrint(A)

print('\nSECOND MATRIX')
p=int(input("Enter Number of Columns : "))
B=MatrixInput(n,p)
MatrixPrint(B)


C=[]
for i in range(m):
    temp=[]
    for k in range(p):
        s=0
        for j in range(n):
            s+=A[i][j]*B[j][k]
        temp.append(s)
    C.append(temp)

print("\nProduct")
MatrixPrint(C)

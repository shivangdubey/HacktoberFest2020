import numpy as np

def createMatrix(row):
    mat1 = []
    for i in range(row):
        k = np.array(list(map(float, input(f"enter element of row number {i+1} seperated by space : ").strip().split())))
        mat1.append(k)
    mat1 = np.array(mat1)
    return mat1

print("dimension := rows x columns")
n1, m1 = list(map(int,input("enter dimension of first matrix with a space: ").strip().split()))
n2, m2 = list(map(int,input("enter dimension of second matrix with a space: ").strip().split()))

mat1 = createMatrix(n1)
mat2 = createMatrix(n2)

print(np.matmul(mat1,mat2))

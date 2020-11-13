

import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    diagonal1 = 0
    diagonal2 = 0
    for i in range(len(arr)):
        diagonal1 += arr[i][i]
        diagonal2 += arr[i][len(arr)-i-1]
    return(abs(diagonal1- diagonal2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

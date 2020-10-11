'''
Problem Statement: Given two sorted arrays, A and B,
determine their intersection. What elements are common to A and B?
'''

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# One line solution
#print(set(A).intersection(B))

def intersection_arrays(A, B):
    i = 0
    j = 0
    intersection = list()

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


print(intersection_arrays(A, B))
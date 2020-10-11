'''
Problem Statement: Given an array of integers, return True or False
if the array has two numbers that add up to a specific target. You may
assume that each input would have exactly one solution.
'''

# Method-1
# Time complexity: O(n^2)
# Space complexity: O(1)

def two_sum1(A, sum):
    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == sum:
                print(A[i], A[j])
                return True
    return False

# Method-2
# Time complexity: O(n)
# Space complexity: O(n)

def two_sum2(A, sum):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[sum - A[i]] = A[i]
    return False

# Method-3
# Time complexity: O(n)
# Space complexity: O(1)

def two_sum3(A, sum):
    i = 0
    j = len(A) - 1
    while i<j:
        if A[i] + A[j] == sum:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < sum:
            i += 1
        else:
            j -= 1
    return False

A = [-2, 1, 2, 4, 7, 11]
target = 13
print(two_sum1(A, target))
print(two_sum2(A, 20))
print(two_sum3(A, 13))
'''
Problem Statement: Is it possible to advance from the start of the array
to the last element given that the maximum you can advance from a position
is based on the value of the array at the index you are currently present on?
'''

def arr_advance(A):
    i = 0
    furthest_reach = 0
    lst_index = len(A) - 1
    while i <= furthest_reach and furthest_reach < lst_index:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1
    return furthest_reach >= lst_index

# True: Possible to navigate to last index in A:
A = [3, 3, 1, 0, 2, 0, 1]
print(arr_advance(A))

# False: Not possible to navigate to last index in A:'
A = [3, 2, 0, 0, 2, 0, 1]
print(arr_advance(A))
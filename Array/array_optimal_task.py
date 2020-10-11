'''
Problem Statement: Assign tasks to workers so that the time it takes
to complete all the tasks is minimized given a count of workers and an
array where each element indicates the duration of a task.
Each worker must work on exactly two tasks.
'''

A = [5, 6, 1, 8, 3, 8]
A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
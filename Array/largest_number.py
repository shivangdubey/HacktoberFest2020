'''
This simple program prints out the largest number in the array.
Edit the arr in function below and replace it with array of your choice.
'''

arr = [23, 56, 345, 7, 99]


def largest(arr, n):
    
    max = arr[0]
    
    for i in range(1,n):
        if arr[i]>max:
            max = arr[i]
    return max


n = len(arr)
print(largest(arr,n))

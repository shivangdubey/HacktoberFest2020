'''
Program for Trapping Rain Water Problem asked by many Product Based Companies like Amazon, Microsoft, Adobe, DE Shaw etc.
Time Complexity: O(n)
Space Complexity: O(1) 
'''


def maxWater(arr, n): 
    '''
    Function to return the maximum water that can be stored
    '''
    size = n - 1
    prev = arr[0] 
  
    # To store previous wall's index 
    prev_index = 0
    water = 0
  
    temp = 0
    for i in range(1, size + 1): 
        if (arr[i] >= prev): 
            prev = arr[i] 
            prev_index = i 
            temp = 0
        else:
            water += prev - arr[i]  
            temp += prev - arr[i] 
  
    if (prev_index < size): 
  
        water -= temp 
        prev = arr[size] 
  
        for i in range(size, prev_index - 1, -1): 
  
            if (arr[i] >= prev): 
                prev = arr[i] 
            else: 
                water += prev - arr[i] 
  
    # Return water 
    return water 
  
#Main 
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] 
n = len(arr) 
print(maxWater(arr, n)) #output 6


  
# Code by Shubham Sharma

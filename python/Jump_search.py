import math 
  
def jump_Search(array,x,n): 
    a = math.sqrt(n) 
    b = 0
    while array[int(min(a, n)-1)] < x: 
        b = a 
        a += math.sqrt(n) 
        if b >= n: 
            return -1
    while array[int(b)] < x: 
        b += 1
        
        if b == min(a, n): 
            return -1
      
 
    if array[int(b)] == x: 
        return b 
      
    return -1
array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ] 
x = 55
n = len(arr) 
index = jump_Search(array, x, n) 
print("Number" , x, "is at index" ,"%.0f"%index) 
  
'''
75. Sort Colors (Medium)
 
i/p :=  [2, 0, 2, 1, 1]
o/p :=  [0, 1, 1, 2, 2]

Explaination :- Sort the array such that all zeros are at start , ones in the middle and 2's at the end of the array


'''


class Solution:
    def sortColors(self, arr):
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(arr)-1
        mid =0
        while(mid <= high):
            if arr[mid] ==0:
                arr[low],arr[mid] = arr[mid],arr[low]
                mid +=1
                low +=1
            elif arr[mid] ==1:
                mid +=1
            else:
                arr[high],arr[mid] = arr[mid] , arr[high]
                high-=1
                
                
if __name__ == '__main__':
    s = Solution()
    arr = list(map(int , input("Enter List")))
    print(arr)
    s.sortColors(arr)
    print(arr)
    #print( "No. Of insertions required to make string palindrome are -> " , s.minInsertions(s1))                
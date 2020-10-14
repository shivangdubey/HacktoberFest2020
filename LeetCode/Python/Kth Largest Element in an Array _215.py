'''
215. Kth Largest Element in an Array (Medium)

i/p := [3,2,1,5,6,4] and k = 2
o/p := 5

'''

class Solution:

    def findKthLargest(self, nums, k: int):
        return sorted(nums , reverse = True)[k-1]
    
if __name__ == '__main__':
    s = Solution()
    arr = list(map(int , input("Enter List")))
    k = int(input())
    print(s.findKthLargest(arr,k))
        
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count

#using hashMap 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        hashMap = {}
        res = 0

        for number in nums:
            if number in hashMap:
                res += hashMap[number]
                hashMap[number] += 1
            else:
                hashMap[number] = 1

        return res

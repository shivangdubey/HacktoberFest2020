class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        new_list = []
        j = 0
        for i in nums:
            j += i
            new_list.append(j)
        return new_list

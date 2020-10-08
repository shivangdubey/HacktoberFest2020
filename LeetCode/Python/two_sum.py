class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #using hashmap
        complementMap = {}

        for i in range (len(nums)):
            num = nums[i]
            complement = target - nums[i]

            if num in complementMap:
                return [complementMap[num] , i]

            else:
                complementMap[complement] = i

    def brute_force(self, nums, target):
        for i in range(len(nums)):

            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:

                    return [i,j]


if __name__ == '__main__':
    nums = [2, 3, 7, 11, 15]
    target = 9
    instance = Solution()
    solution = instance.twoSum(nums, target)
    print(solution)

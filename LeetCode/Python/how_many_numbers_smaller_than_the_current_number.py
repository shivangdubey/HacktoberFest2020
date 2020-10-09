class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """


        count = []
        for i, num in enumerate(nums):
            count.append(len([num_ for num_ in nums if num > num_ ]))
        return count

    def smallerNumbersThanCurrent_Fast(self, nums: List[int]) -> List[int]:
        d = {}
        for i in range(101):
            d[i] = 0
        for num in nums:
            d[num] += 1
        prev = 0
        for item in d:
            if d[item] != 0:
                temp = d[item]
                d[item] = prev
                prev += temp
        for i in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums


if __name__ == '__main__':

    nums = [2,6,4,8,10,9,9]
    nums = [1,3,2,2,2]
    nums = [8,1,2,2,3]

    instance = Solution()
    solution = instance.smallerNumbersThanCurrent(nums)
    print(solution)

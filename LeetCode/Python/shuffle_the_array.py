class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        new_list = []
        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[i+n]) 

        return new_list


if __name__ == '__main__':

    nums = [2,5,1,3,4,7]
    n = 3
    instance = Solution()
    solution = instance.shuffle(nums , n)
    print(solution)

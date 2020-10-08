class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # lst = []
        # index = []
        # #check if ith num is greater than the following num
        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1] :
        #         lst.append(nums[i])
        #         index.append(i)
        #
        # # if len(lst) > 0:
        # #     length = lst[-1] - lst[0] + 2
        # # else:
        # #     length  = 0
        #
        # return  lst, index
        count_dict = {}
        set_nums = []
        for num in nums:
            if num not in count_dict:
                count_dict[num] = 1
                set_nums.append(num)
            else:
                count_dict[num] += 1


        lst = []
        index = []
        #for every case except the last one
        for i in range(1, len(set_nums)):
            if set_nums[i] < set_nums[i-1] :
                lst.append(set_nums[i])
                index.append(i)
        #for the last case
        if set_nums[0] > set_nums[1] :
            lst.insert(0,set_nums[0])
            index.insert(0,0)

        unsorted = set_nums[index[0]:index[-1]+1]
        count = 0
        for i, num in enumerate(unsorted):
            count += count_dict[num]
        print(count)

        print( 'count_dict: ' count_dict , 'set_nums: ', set_nums, 'lst', lst, index, set_nums[index[0]:index[-1]+1])

if __name__ == '__main__':

    nums1 = [2,6,4,8,10,9,9]
    nums2 = [1,3,2,2,2]
    nums3 = [4,2,2,2,3,1,9]
    nums4 = [1,2,3,3,3]
    instance = Solution()
    solution = instance.findUnsortedSubarray(nums3)
    print(solution)

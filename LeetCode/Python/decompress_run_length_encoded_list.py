class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        range_ = int(len(nums)/2)

        for i in range(range_):
            temp_list = []
            freq = nums[2*i]
            val  =  nums[2*i+1]
            temp_list.append(val)
            new_list = new_list + temp_list*freq

        return new_list

    def decompressRLElist_Faster(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i+1]] * nums[i]
        return res

if __name__ == '__main__':

    nums = [1,2,3,4]

    instance = Solution()
    solution = instance.decompressRLElist(nums)
    print(solution)

[]+[1]

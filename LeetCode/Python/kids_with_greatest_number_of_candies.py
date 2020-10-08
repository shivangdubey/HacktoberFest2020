class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sorted_list = sorted(candies, reverse = True)
        return [candy + extraCandies >= sorted_list[0] for candy in candies]


    def kidsWithCandies_Faster(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [candy + extraCandies >= max(candies) for candy in candies]

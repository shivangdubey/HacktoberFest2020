"""
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.
Suppose the stones have weights x and y with x <= y.
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
"""


class Solution:
    def lastStoneWeight(self, stones) -> int:
        """
        Remove two heaviest element and append abs diff of two
        repeat till array len is 1
        """
        n = len(stones)

        while n > 1:
            i = max(stones)
            stones.remove(i)

            j = max(stones)
            stones.remove(j)

            stones.append(abs(i - j))

            n = len(stones)

        return stones[0]


print(Solution().lastStoneWeight([1, 2, 3, 4, 5]))

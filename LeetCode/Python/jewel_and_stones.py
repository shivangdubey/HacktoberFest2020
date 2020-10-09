class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        count = 0
        for char in S:
            if char in J:
                count +=1
        return count


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    instance = Solution()
    solution = instance.numJewelsInStones(J,S)
    print(solution)

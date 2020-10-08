class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        j = 0
        for i in range(2, len(s)+1, 2):
            if  s[j:i].count('L') == s[j:i].count('R'):
                count += 1
                j = i

        return count

    def balancedStringSplit_easy(self, s: str) -> int:
            balancedCount = count = 0
            for char in s:
                if char == 'L':
                    count += 1
                elif char == 'R':
                    count -= 1
                if count == 0:
                    balancedCount += 1
            return balancedCount



if __name__ == '__main__':

    input = "RLRRRLLRLL"
    instance = Solution()
    solution = instance.balancedStringSplit(input)
    print(solution)

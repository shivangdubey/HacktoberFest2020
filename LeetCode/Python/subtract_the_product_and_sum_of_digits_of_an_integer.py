class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in range(len(str(n))):
            product *= n%10
            sum += n%10
            n = n//10
            
        return product - sum


if __name__ == '__main__':

    n = 234
    instance = Solution()
    solution = instance.subtractProductAndSum( n)
    print(solution)

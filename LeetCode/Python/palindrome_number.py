class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = int(x)
        r = 0
        while x > 0:
            r *= 10
            r += x % 10
            x //= 10
        print(r)

        if r == y:
            return True
        else:
            return False

if __name__ == '__main__':

    x = 929
    instance = Solution()
    solution = instance.isPalindrome(x)
    print(solution)

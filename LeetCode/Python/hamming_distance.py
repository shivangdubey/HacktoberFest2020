class Solution(object):
    def binarydigit(self, n):
        binary = ''
        while n > 0:
            binary += str(n%2)
            n //= 2
        return binary[::-1]

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        binary_x = self.binarydigit(x)
        binary_y = self.binarydigit(y)

        len_x = len(binary_x)
        len_y = len(binary_y)

        if len_x > len_y:
            binary_y = (len_x - len_y)* '0' + binary_y

        if len_x < len_y:
            binary_x = (len_y - len_x)* '0' + binary_x

        counter = 0
        for i in range(len(binary_x)):
            if binary_x[i] != binary_y[i]:
                counter += 1



        return counter


    def hammingDistance_short_solution(self, x: int, y: int) -> int:

        res=x^y
        res_bin = bin(res).split('b')[1]

        cnt=0

        for i in range(len(res_bin)):
            if res_bin[i]=='1':
                cnt+=1

        return cnt


    def hammingDistance_one_liner(self, x, y):
        return bin(x^y).count('1')


if __name__ == '__main__':
print(solution)
    x = 1
    y = 4
    instance = Solution()
    %timeit solution_me = instance.hammingDistance(x , y)
    %timeit solution_short = instance.hammingDistance_short_solution(x, y)
    %timeit solution_one_liner = instance.hammingDistance_one_liner(x, y)

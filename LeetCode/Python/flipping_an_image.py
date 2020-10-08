nparray1 = ([1, 1]) # Define an array
nparray2 = ([4, 5])
flavor4 = 0
for a, b in zip(nparray1, nparray2):
    flavor4 += a * b
flavor4

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        len_A = len(A)
        for i in range(len_A):
            A[i] = A[i][::-1]

        for i in range(len_A):
            for j in range(len_A):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A

    # def flipAndInvertImage_fast(self, A):
    #     for i in range(len(A)):
    #         l, r = 0, len(A[i]) - 1
    #         while l <= r:
    #             # Solution 1: Time: 99.94%, Space: 5.61%
	# 			A[i][l], A[i][r] = 0 if A[i][r] else 1, 0 if A[i][l] else 1
	# 			# Solution 2: Time: 38.71%, Space: 51.40%
	# 			# A[i][l], A[i][r] = int(not A[i][r]), int(not A[i][l])
	# 			# Solution 3: Time: 92.01% Space: 61.60%
	# 			# A[i][l], A[i][r] = A[i][r]^1, A[i][l]^1
    #             l += 1
    #             r -= 1
    #     return A
    def flipAndInvertImage_oneliner(self, A: List[List[int]]) -> List[List[int]]:

        return [list(reversed([1 if j==0 else 0 for j in i])) for i in A]

if __name__ == '__main__':

    input =  [[1,1,0],[1,0,1],[0,0,0]]
    instance = Solution()
    solution = instance.flipAndInvertImage(input)
    print(solution)

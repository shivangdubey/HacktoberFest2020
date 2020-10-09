class Solution:
    def isValid(self, s: str) -> bool:

        open_list = ["[","{","("]
        close_list = ["]","}",")"]

        # Function to check parentheses

        stack = []
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False



        # dict = {'{':'}',
        #         '[':']',
        #         '(':')' }

        # odd_list = [s[j] for j in range(0,len(s),2)]+ [s[-1]]
        # print(odd_list)
        #
        # for br in s:
        #     if dict[br]
        # s_list_fhalf = s[:len(s)//2]
        # s_list_lhalf = s[len(s)//2:]
        #
        # error = []
        # for f , l in zip(s_list_fhalf,s_list_lhalf[::-1]):
        #     if l == dict[f]:
        #          error.append(0)
        #     else:
        #         error.append(1)
        # return error


if __name__ == '__main__':

    x = "([{[]}]])"
    # x = str("()[][]")
    instance = Solution()
    solution = instance.isValid(x)
    print(solution)

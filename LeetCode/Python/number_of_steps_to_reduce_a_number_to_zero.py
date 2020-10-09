class Solution:
    def numberOfSteps (self, num: int) -> int:

        step_count = 0
        for i in range(num):
            if num != 0:

                if num %2 == 0:
                    print(f'{num} is even; divide by 2 and obtain {num/2}')
                    num /= 2

                else:
                    print(f'{num} is odd; subtract 1 and obtain {num - 1}')
                    num -= 1

                step_count += 1

            else:
                break

        return step_count


if __name__ == '__main__':

    n = 14
    instance = Solution()
    solution = instance.numberOfSteps(n)
    print(solution)

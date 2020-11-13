class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        cal = run = 0
        tem = s[:cal]
        for i in range(len(s)):
            cal += 1
            tem = s[:cal]

            # Jump is with the size of searching elelment i.e cal
            for j in range(cal, len(s), cal):
                if tem == s[j: j + cal]:
                    run = j + cal
                    if run == len(s):
                        return True
                else:
                    break
        return False

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length=len(palindrome)
        for i in range(0,length//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
        return palindrome[:-1]+'b' if length!=1 else ""
            
                
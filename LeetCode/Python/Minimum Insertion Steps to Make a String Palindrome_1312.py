'''
1312. Minimum Insertion Steps to Make a String Palindrome (Hard)

i/p : zzazz
o/p : 0
Explaination :- As string itself is a plaindrom , so 0 insertions are required

'''

class Solution:
    def solve(self , s1 , s2 , n ,m ,t):
        if n==0 or m==0:  # if length of string 1 or string2 is 0 , return 0
            return 0
        if t[n][m] !=-1:   # if value is already present in table , no need for a recursive call
            return t[n][m]
        
        if s1[n-1] == s2[m-1]:  # if last char of string 1 and string 2 are same  
            t[n][m] = 1 + self.solve(s1,s2,n-1,m-1,t)
            return t[n][m]
        else:
            t[n][m] = max( self.solve(s1,s2,n-1,m ,t) , self.solve(s1,s2,n,m-1 ,t)) # if last 2 characters are not same
            return t[n][m]
    
    def minInsertions(self, s1: str) -> int:
        if len(s1)<=1:
            return 0
        s2 = s1[::-1]  # reversing sring
        n = len(s1)
        t = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return n - self.solve(s1,s2,n,n ,t)
    
if __name__ == '__main__':
    s = Solution()
    s1 = input("Input String :- ")
    print( "No. Of insertions required to make string palindrome are -> " , s.minInsertions(s1))
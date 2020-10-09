'''
62. Unique Paths(Medium)
i/p :=  m = 3, n = 2
o/p := 3

Explaination := From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

i.e count steps required to reach from  0,0  to given point 
'''

class Solution:
     
    def uniquePaths(self, nr: int, nc: int) -> int:
        
        grid = [[0 for _ in range(nc+1)]for _ in range(nr+1)]
        for i in range(nr):
            grid[i][0] = 1  #if only 1 row is present then bot can move directly in right direction
            
        for j in range(nc): #if only 1 col is present then bot can move directly in bottom direction
            grid[0][j] = 1

        for i in range(1,nr):
            for j in range(1, nc):
                grid[i][j] = grid[i-1][j] + grid[i][j-1] # can move either right or down
        return (grid[nr-1][nc-1])

if __name__ == '__main__':
    s = Solution()
    m = int(input())
    n = int(input())
    print("Steps required are :- ",s.uniquePaths(m,n))
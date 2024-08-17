class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for i in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        def solve(i, j):
            if dp[i][j]:
                return dp[i][j]
            dp[i][j]=solve(i-1,j)+solve(i,j-1)
            return dp[i][j]
        return solve(m-1,n-1)
        

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]*len(text2) for i in range(len(text1))]
        def solve(i, j):
            if i==-1 or j==-1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j]=1+solve(i-1, j-1)
                return dp[i][j]
            dp[i][j]=max(solve(i-1, j), solve(i, j-1))
            return dp[i][j]
        return solve(len(text1)-1, len(text2)-1)

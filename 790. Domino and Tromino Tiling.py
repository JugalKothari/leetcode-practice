class Solution:
    def numTilings(self, n: int) -> int:
        dp=[0] * (n+1)
        dp[0]=1
        def solve(index):
            if dp[index]!=0:
                return dp[index]
            if index==1 or index==2:
                dp[index]=index
                return index
            dp[index] = (solve(index-1)*2) + solve(index-3)
            return dp[index]
        return solve(n)%(10**9+7)
            

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[-1]*2 for i in range(len(prices))]
        def solve(index, buy):
            if index==len(prices):
                return 0
            if dp[index][buy]!=-1:
                return dp[index][buy]
            if buy:
                dp[index][buy] = max(-prices[index] + solve(index+1, 0), solve(index+1,1))
            else:
                dp[index][buy] = max(prices[index] + solve(index+1, 1) - fee, solve(index+1, 0))
            return dp[index][buy]
        return solve(0,1)

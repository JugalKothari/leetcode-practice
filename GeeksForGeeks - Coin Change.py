def findMinCoins(coins: [], target: int) -> int:
    dp=[target+1] * (target+1)
    dp[0]=0

    for amount in range(1,target+1):
        for coin in coins:
            if amount-coin >=0:
                dp[amount] = min(dp[amount], 1 + dp[amount-coin])
    return dp[target] if dp[target]!=(target+1) else -1

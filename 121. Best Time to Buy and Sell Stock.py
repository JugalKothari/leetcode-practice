class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1=0
        p2=1
        profit=0
        while p2<len(prices) and p1<p2:
            if prices[p2]-prices[p1]>profit:
                profit=prices[p2]-prices[p1]
            elif prices[p2]-prices[p1]<0:
                p1=p2
            elif prices[p2]-prices[p1]==0:
                pass
            else:
                pass
            p2+=1
            
        return profit

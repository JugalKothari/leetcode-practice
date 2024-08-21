class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost=sum(cost)
        total_gas=sum(gas)
        if total_gas<total_cost:
            return -1
        
        ans=0
        cur_gas=0
        for i in range(len(gas)):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                cur_gas=0
                ans=i+1
        return ans

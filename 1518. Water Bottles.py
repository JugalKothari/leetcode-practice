class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        maxdrink=numBottles
        emptybottles=numBottles
        numBottles=emptybottles//numExchange 
        emptybottles=emptybottles%numExchange
        while numBottles>=1:
            maxdrink+=numBottles
            emptybottles+=numBottles
            numBottles=emptybottles//numExchange
            emptybottles=emptybottles%numExchange
            
        return maxdrink
      

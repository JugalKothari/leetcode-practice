class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        units=0
        for item in boxTypes:
            if truckSize<=0:
                return units
            units+=min(truckSize, item[0])*item[1]
            truckSize-=item[0]
        return units
      

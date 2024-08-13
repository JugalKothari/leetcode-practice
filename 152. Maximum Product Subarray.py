class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct=max(nums)
        currmin=1
        currmax=1
        for num in nums:
            if num==0:
                currmax, currmin = 1, 1
                continue
            temp = currmax*num
            currmax = max(temp, currmin*num, num)
            currmin = min(temp, currmin*num, num)
            maxproduct = max(maxproduct, currmax)
        return maxproduct

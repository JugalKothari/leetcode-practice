class Solution(object):
    def pivotIndex(self, nums):
        n=len(nums)
        lsum=0
        rsum=sum(nums)
        for i in range(n):
            rsum=rsum-nums[i]
            if lsum==rsum:
                return i
            else:
                lsum=lsum+nums[i]
        return -1 

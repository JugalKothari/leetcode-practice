class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        right=0
        zeros=0
        maxl=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeros+=1
            if zeros>1:
                if nums[left]==0:
                    zeros-=1
                left+=1
            maxl=max(maxl,right-left)
        return maxl

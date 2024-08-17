class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]
        def solve(index):
            if index==len(nums):
                return
            if index==1:
                dp[index]=max(nums[0], nums[1])
                solve(index+1)
                return
            dp[index]=max(dp[index-2]+nums[index], dp[index-1])
            solve(index+1)
        solve(1)
        return dp[len(nums)-1]

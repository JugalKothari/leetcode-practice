class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left=float("inf")
        mid=float("inf")
        for i in range(len(nums)):
            if nums[i]<=left:
                left=nums[i]
            elif nums[i]<=mid:
                mid=nums[i]
            else:
                return True
        return False

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tempsums=[nums[0]]
        for i in range(1,len(nums)):
            if tempsums[i-1]+nums[i]>nums[i]:
                tempsums.append(tempsums[i-1]+nums[i])
            else:
                tempsums.append(nums[i])
        print(tempsums)
        return max(tempsums)

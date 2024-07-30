class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx1=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                idx1=i
                break
        if idx1==-1:
            return nums.reverse()
        else:
            idx2=-1
            for j in range(len(nums)-1, idx1, -1):
                if nums[j]>nums[idx1]:
                    idx2=j
                    break
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            nums[idx1+1:] = sorted(nums[idx1+1:])
            return nums

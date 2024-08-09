class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start=0
        end=0
        count=0
        counts=[]
        while end<len(nums):
            if nums[end]==1:
                count+=1
                end+=1
            else:
                counts.append(count)
                count=0
                start=end+1
                end=start
        counts.append(count)
        return max(counts)

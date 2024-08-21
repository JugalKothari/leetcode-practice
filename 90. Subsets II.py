class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        power_set=[]
        nums.sort()
        def subsets(index, subseq):
            if index>=len(nums):
                power_set.append(subseq[:])
                return
            
            subseq.append(nums[index])
            subsets(index+1, subseq)
            while index+1<len(nums) and nums[index]==nums[index+1]:
                index+=1
            subseq.pop()
            subsets(index+1, subseq)
        
        subsets(0, [])
        return sorted(power_set)
      

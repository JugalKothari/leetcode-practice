class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        srted=sorted(nums)
        left=0
        right=len(srted)-1
        ops=0
        while left<right:
            sum=srted[left]+srted[right]
            if sum==k:
                ops+=1
                left+=1
                right-=1
            elif sum<k:
                left+=1
            else:
                right-=1
        return ops

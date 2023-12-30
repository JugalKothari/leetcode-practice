class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        ans=sum(nums[:k])
        maxavg=ans/k
        for start in range(k,n):
            ans=ans+nums[start]-nums[start-k]
            avg=ans/k
            maxavg=max(avg,maxavg)
            start+=1
        return maxavg

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyds tortoise and hare algorithm
        slow=nums[0]
        fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        p=nums[0]
        while p!=slow:
            p=nums[p]
            slow=nums[slow]
        return p

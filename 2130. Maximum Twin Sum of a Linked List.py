# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l1=list()
        while head!=None:
            l1.append(head.val)
            head=head.next
        maxsum=0
        mid = len(l1)//2
        sums=[]
        while mid>0:
            sums.append(l1[mid-1]+l1[-mid])
            mid-=1
        return max(sums)
        

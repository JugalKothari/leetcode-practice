# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i=0
        l3=head=ListNode()
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            sum=val1+val2+carry
            l3.next=ListNode(val = sum%10)
            l3=l3.next
            carry=sum//10
            if l1: l1=l1.next
            if l2: l2=l2.next

        return head.next
        

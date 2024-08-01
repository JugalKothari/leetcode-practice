# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h=head
        length=0
        while head:
            length+=1
            head=head.next
        if length==1:
            return head
        if length==n:
            return h.next
        head=h
        i=0
        while head.next:
            if length-i==n+1:
                head.next=head.next.next
                break
            else:
                head=head.next
                i+=1
        return h
        

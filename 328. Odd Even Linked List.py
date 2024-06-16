# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:return None
        p=head
        r=q=head.next
        while q and q.next:
            p.next=p.next.next
            q.next=q.next.next
            p=p.next
            q=q.next
        p.next=r
        return head
        

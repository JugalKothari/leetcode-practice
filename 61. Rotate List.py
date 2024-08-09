# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        curr=head
        length=0
        while curr:
            curr=curr.next
            length+=1
        k=k%length
        while k>0:
            newtail=head
            newsecond=head
            while newtail.next.next is not None:
                newtail=newtail.next
            temp=newtail.next
            newtail.next=None
            temp.next=newsecond
            head=temp
            k-=1
        return head
        

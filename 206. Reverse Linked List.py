# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        h=head
        while head!=None:
            values.append(head.val)
            head=head.next
        head=h
        while head!=None:
            head.val=values.pop()
            head=head.next
        return h

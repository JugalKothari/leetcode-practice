# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #floyd tortoise and hare algorithm
        tortoise=head
        hare=head
        while hare and hare.next:
            tortoise=tortoise.next
            hare=hare.next.next
            if tortoise==hare:
                break
        if hare is None or hare.next is None:
            return None
        p0=head
        while p0 != tortoise:
            p0 = p0.next
            tortoise = tortoise.next
        return p0
      

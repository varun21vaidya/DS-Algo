# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # method 1 floyds cycle detection algo,
        # take two pointers, slow amd fast , fast moves with 2 steps at a time,
        # once the both pointers meet ie slow==fast we can assure loop exists
        # now as loop exists, reinitialize slow to head, 
        # and now move both pointers one step at a time,
        # their meeting point will be start of loop
        
        slow,fast=head,head
        loop=False
        while fast and fast.next:
            
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                loop=True
                break
        if loop:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        else:  
            return None
         
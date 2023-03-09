# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return 
        loop=False
        slow,fast=head,head
        
        # first check if its loop or not:
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                loop=True
                break
                
        # if there is loop, we will reinitialize slow pointer and
        # fast will also move 1 step at a time
        # meeting of them will be our ans
        
        if loop:
            slow= head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        else:
            return 
        
        
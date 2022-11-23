# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         # method 1: sett TC: O(n) SC: O(n)
#         sett=set()
        
#         # run until head becomes null
#         while head:
            
#             # if node is in sett, its a cycle, return True
#             if head in sett:
#                 return True
            
#             # else add the node to sett and traverse list
#             sett.add(head)
#             head=head.next
        
#         # if head becomes null gets out of while loop
#         # it does not contain a cycle
#         return False
    
        # Method 2: Floyd's Algo TC: O(n) SC: O(1)
        
        # Now we can also do this, in constant time
        # with Floyd’s Cycle-Finding Algorithm
        # with using two pointers one uses 1 step at a time
        # other moves 2 steps at a time
        # if they both meet at any point, its a cycle
        # else p2 will result null and return False
        
        p1, p2 = head, head
        while p1 and p2 and p2.next:
            p1=p1.next
            p2=p2.next.next
            if p1==p2:
                return True
        
        return False
        
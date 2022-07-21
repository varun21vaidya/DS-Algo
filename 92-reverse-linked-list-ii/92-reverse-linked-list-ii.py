# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int):       
        if not head or not head.next or left == right:
            return head
        
        dummy_head = ListNode(val=-1, next=head)
        p_prev = dummy_head
        
        # Iterate p_prev to the (left-1)-th node
        for _ in range(left - 1):
            p_prev = p_prev.next
            
        p_cur = p_prev.next # p_cur is at the left-th node
        
        # Within the reverse part, iteratively move the next node of p_cur to the beginning
        for _ in range(right - left):
            p_next = p_cur.next
            p_cur.next = p_next.next
            p_next.next = p_prev.next
            p_prev.next = p_next
        
        return dummy_head.next
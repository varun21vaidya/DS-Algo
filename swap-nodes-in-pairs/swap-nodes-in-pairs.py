# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(head):
            if (head==None) or (head.next==None):
                return
            head.val,head.next.val=head.next.val,head.val
            swap(head.next.next)
            
        temp=head
        swap(head)
        return temp
        
        
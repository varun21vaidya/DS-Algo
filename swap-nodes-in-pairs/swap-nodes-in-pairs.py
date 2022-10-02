# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(head,temp):
            if (head==None) or (head.next==None):
                return temp
            head.val,head.next.val=head.next.val,head.val
            swap(head.next.next,temp)
            
        temp=head
        swap(head,temp)
        return temp
        
        
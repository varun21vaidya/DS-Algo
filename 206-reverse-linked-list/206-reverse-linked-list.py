# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev,temp,curr=None,None,head
        # while curr:
        #     temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=temp
        # return prev
        
        
        # Recursive 
        
        if not head or not head.next: return head
        
        newhead=self.reverseList(head.next)
        head.next.next=head
        head.next = None
        return newhead
            
        
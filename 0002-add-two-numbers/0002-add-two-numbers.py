# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=res=ListNode()
        total=0
        prev=0
        
        while l1 or l2: 
            
            total=prev
            
            if l1:
                total+=l1.val
                l1=l1.next
                
            if l2:
                total+=l2.val
                l2=l2.next
                
            if total>=10:
                total-=10
                prev=1
            else:
                prev=0
                
            res.next=ListNode(total)
        
            res=res.next
       
        if not l1 and not l2 and prev:
            res.next=ListNode(prev)
            
        return temp.next
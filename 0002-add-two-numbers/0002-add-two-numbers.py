# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=res=ListNode()
        prev=0
        while l1 and l2: 
            node=l1.val+l2.val+prev
            l1=l1.next
            l2=l2.next
            
            if node<10:
                res.next=ListNode(node)
                prev=0
            else:
                res.next=ListNode(node-10)
                prev=1

            res=res.next
        
        while l1:
            node=l1.val+prev
            l1=l1.next
            
            if node<10:
                res.next=ListNode(node)
                prev=0
            else:
                res.next=ListNode(node-10)
                prev=1
            

            res=res.next
        while l2:
            node=l2.val+prev
            l2=l2.next
            
            if node<10:
                res.next=ListNode(node)
                prev=0
            else:
                res.next=ListNode(node-10)
                prev=1
                
            res=res.next 
            
        if prev:
            res.next=ListNode(prev)
            
        return temp.next
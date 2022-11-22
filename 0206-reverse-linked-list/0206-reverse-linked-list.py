# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#       Iterative Solution

        # curr,prev,nextt=head,None,None
        # while curr:
        #     nextt=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=nextt
        # return prev
        
#       Recursive Solution TOP-->DOWN
        
        # def solver(curr,prev):
        #     if curr:
        #         nextt=curr.next
        #         curr.next=prev
        #         return solver(nextt,curr)
        #     else:
        #         return prev
        # return solver(head, None)
        
        
#       Recursive Bottom-->UP
        
        # create a newhead and it will point to previous node which is current head
        # and that current head will point to null
        # base condition: if head or head.next is null return head
        # and when newhead is returned head.next.next will point to head
        # and head.next will point to null so at each point last node will point to null
        # and at the end first node will point to null and all others would be pointing to it
        
#         ie og linkedlist and newhead will be perpendicular at head point
#         when head=5 return head, newhead=5
#                                         5                     
#                                         |
#         newhead=5, head=4 output= 1-2-3-4-None
#         now return newhead=5>4
        
#                                       5                     
#                                       4  
#         newhead=4, head=3 output= 1-2-3-None
#         now return newhead=5>4>3
#                                     5
#                                     4                     
#                                     3 
#         newhead=3, head=2 output= 1-2-None
#         now return newhead=5>4>3>2  
#                                   5
#                                   4
#                                   3                     
#                                   2 
#         newhead=2, head=1 output= 1-None
#         now return newhead= 5>4>3>2>1
        
        
        if head==None or head.next == None: return head
        
        newhead= self.reverseList(head.next)
        head.next.next=head
        head.next=None
        
        return newhead
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # prev,temp,curr=None,None,head
        # while curr:
        #     temp=curr.next
        #     curr.next=prev
        #     prev=curr
        #     curr=temp
        # return prev
        
        
    # # Its Recursive Solution
    
#         def solver(curr,prev):
            
#             if curr:
#                 temp=curr.next
#                 curr.next=prev
                
#                 return solver(temp,curr)
#             else:
#                 return prev
                
#         return solver(head,None)
    
    
    
    
        # Recursive 2
        
            # nice ref with diagram
            # https://leetcode.com/problems/reverse-linked-list/discuss/2105240/Reverse-Linked-List-oror-Easy-recursive-solution-with-image-explanation

            # so if the next node is Null Return the head
            # so take example for 1 2 3 4 5
            # at the end for head 4 it will call recursive fn with head5
            # which will give null for head.next and return head
            # so newhead will be 5
            # and head is 4 when got out of backtracking
            # so head.next.next which was null will now point to head again
            # and head.next will point to null
            # so 1-->2-->3-->4--None and 5-->4
            # now return newhead which is 5 ie 5-->4
            # so again it will get out of backtrack to head = 3
            # so head.next.next = head ie 4-->3 and 3-->None
            # and og list will be 1-->2-->3-->None 
            # and 4 pointing to 3 which is from newhead => 5-->4-->3-->None
            # so like that ref from og list gets attached to newhead 
            # and newhead will become 5-->4-->3-->2-->1-->None
        
        
#         if not head or not head.next: return head
        
#         newhead=self.reverseList(head.next)
#         head.next.next=head
#         head.next = None
#         return newhead
            
        
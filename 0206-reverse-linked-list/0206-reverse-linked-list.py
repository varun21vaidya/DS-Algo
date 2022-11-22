# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev,nextt=head,None,None
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
            
        
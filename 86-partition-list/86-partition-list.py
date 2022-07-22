# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()  #dummy nodes
        lefttail, righttail =left , right   #ref to dummy nodes   
            
        while head:
            if head.val< x:              #less than x values add to left nodelist
                lefttail.next= head
                lefttail= lefttail.next
                
            else:
                righttail.next = head    #greater than or eaqual to xvalues add to left nodelist
                righttail= righttail.next
                
            
            head= head.next              #move head nodes
            
        #lefttail and righttail are ref to left and right nodes and as they are iterated
        #now they represent last node of left and right lists
        #and left and right are dummy nodes
        #so left.next and right.next defines first nodes of each
        
        lefttail.next = right.next      #connect last node of left list to first of right list
        righttail.next = None           #point last node of right list to Null            
        
        return left.next                #return head of combined list
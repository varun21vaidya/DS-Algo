# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # method 1:
        # 2 pass solution, first calulate lenght of linked list
        # then traverse len-n steps and remove element
        
        # method 2 :
        # reverse linked list remove element at n position reverse and return 
    
        # method 3: 
#         similar to finding middle of linked list
#         use 2 pointers, first of all move first pointer n positions
#         and then move both pointers together, when first pointer points to null
#         then second pointer will be at one position behind the removal node
#         then point second pointer to next of next ie remove the required node
#         as ahead pointer takes one pass to traverse its O(n)
        
        ahead=temp=head
        
        if not head.next: return None
        
        while n>0 and ahead:
            ahead=ahead.next
            n-=1

        if not ahead:
            return head.next
        
        while ahead.next:
            ahead=ahead.next
            head=head.next
            
        
        head.next=head.next.next
        
        return temp
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(2N) - 2 pass solution
#       first traverse whole linked list
#       calculate the length of list
#       and traverse upto half of that length and return 

#         count=0
#         temp=head
#         while temp:
#             temp=temp.next
#             count+=1
#         cnt=count//2
#         while cnt>0:
#             head=head.next
#             cnt-=1
        
#         return head
        
        
        # 2 pointer approach - 1 Pass Solution: O(n)
        # one pointer traverse with 1 step at a time
        # while second pointer moves with 2 steps at time
        # so pointer2 will be double faster and
        # cover double distance than pointer1
        # so when pointer1 is at mid, pointer 2 will be at end
        # so check until pointer2.next for odd length 
        # and pointer2.next.next for even 
        # and traverse both pointers 
        # and after while loop return pointer1
    
        ptr1,ptr2=head,head
        while ptr2.next:
            if not ptr2.next.next:
                ptr1=ptr1.next
                break
            ptr1=ptr1.next
            ptr2=ptr2.next.next
            
        return ptr1
        
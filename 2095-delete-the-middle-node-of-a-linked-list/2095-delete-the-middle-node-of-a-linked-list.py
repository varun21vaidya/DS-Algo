# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
# #       first calculate size of linked list then calculate mid and delete it
# #       loop upto mid-1 and head.next=head.next.next so skip the mid node

#         # TC: O(n) SC: O(1)
#         temp=head
#         if head.next==None:
#             return None
#         size=0
#         while head:
#             size+=1
#             head=head.next
#         mid=size//2
#         head=temp
#         n=0
#         while n<mid-1:
#             n+=1
#             head=head.next
#         head.next=head.next.next
#         return temp


#       Fast and Slow Method:
#       use two pointers at same time, one at double speed, one at normal speed
#       when double speed pointer reaches end and next is None or next.next is None,
#       normal speed pointer is before mid, so we can skip mid and return head
        if not head.next:
            return None
        
        slow,fast=head,head.next

        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            
        slow.next=slow.next.next
        return head
        
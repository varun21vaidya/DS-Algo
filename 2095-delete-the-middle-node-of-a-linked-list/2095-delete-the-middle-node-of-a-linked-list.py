# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head.next==None:
            return None
        size=0
        while head:
            size+=1
            head=head.next
        mid=size//2
        head=temp
        n=0
        while n<mid-1:
            n+=1
            head=head.next
        head.next=head.next.next
        return temp
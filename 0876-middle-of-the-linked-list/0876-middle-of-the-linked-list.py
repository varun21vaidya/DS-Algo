# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            temp=temp.next
            count+=1
        cnt=count//2
        while cnt>0:
            head=head.next
            cnt-=1
        
        return head
        
        
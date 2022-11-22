# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#       first traverse whole linked list
#       calculate the length of list
#       and traverse upto half of that length and return 
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
        
        ptr1,ptr2=head,head
        while ptr2.next or ptr2.next.next:
            ptr1=ptr1.next
            ptr2=ptr2.next.next
        return ptr1
        
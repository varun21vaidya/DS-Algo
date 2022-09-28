# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # (Wrong Logic for now)
#         def getLength(lenn,head):
#             while head:
#                 lenn+=1
#                 head= head.next
#             return lenn
        
#         temp=head
#         length=getLength(0,head)
        
#         for i in range(0,length-n):
#             temp=temp.next
#         if temp==None:
#             temp.next=None
#         else:
#             temp.next=temp.next.next

#         return head

        #define two pointers
        skipper=runner=head

        # first traverse skipper for n positions
        # that way it will be n position ahead of runner which will start later
        for i in range(n):
            skipper=skipper.next

        # if end=n then we have alredy reached n for skipper, then return eg [1] 1
        if not skipper:
            return head.next
        
        # so when skipper reach end, runner will be at end-n position
        while skipper.next:
            skipper=skipper.next
            runner=runner.next

        # so we will skip the runner.next position and link to runner.next.next
        runner.next=runner.next.next
        return head





        
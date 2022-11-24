# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp=head
        
        cnt=0 # length of linked list
        while temp:
            temp=temp.next
            cnt+=1
        # print(cnt)
        
        # count how many times it should loop
        count=cnt//k
        print(count)
        curr,prev,nextt=head,head,None
        
        curr,prev,nextt=head,ListNode(),None
        temp=prev
        prev.next=curr
        for i in range(count):
            for j in range(k-1):
                nextt=curr.next
                curr.next=nextt.next
                nextt.next=prev.next
                prev.next=nextt
            prev=curr
            curr=prev.next
            # print(curr)
                
        return temp.next
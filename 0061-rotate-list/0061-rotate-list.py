# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
                
#         # first traverse k steps in list with p1 pointer
#         # then traverse p2 from start and p1 from k steps at same time
#         # until p1.next reaches Null
#         # when it reaches null, p2 will be k steps behind the end of list
#         # now p1 pointer at end will be redirected to head
#         # and p2 pointers next will point Null 
#         # and original p2.next will be head of list, return it
        
#         # if list is empty return
#         if not head: return head
        
        
#         p1,p2=head,head

#         # but if k is more than length of list
#         # then we need to take mod, ie count of list % k
#         # to get exact iterations of k ie remove extra iterations with mod
        
        
#         # get length of linked list
#         counter=head
#         count=0
#         while counter:
#             counter=counter.next
#             count+=1
          
#         # if single element in list or count and k are equal or multiple of them ie mod,
#         # return list as it is
#         if count==1 or count==k or k%count==0:
#             return head
        
#         # remove extra iterations of k if any
#         k=k%count
        
#         # first traverse k steps in list with p1 pointer
#         while k:
#             p1=p1.next
#             k-=1
        
#         # then traverse p2 from start and p1 from k steps at same time
#         # until p1.next reaches Null
#         while p1.next:
#             p1=p1.next
#             p2=p2.next
        
        
        
#         # when it reaches null, p2 will be k steps behind the end of list
#         # now p1 pointer at end will be redirected to head
#         # and p2 pointers next will point Null 
#         # and original p2.next will be head of list, return it
#         temp=p2.next
#         p1.next=head
#         p2.next=None
#         return temp
        
        
        
        
        # now instead of all this, we can just make a cycle from this list
        # and before that take length of list
        # and take a mod of k with length to avoid extra iterations
        # now traverse length - k steps and just direct that point to null
        
        
        # if list is empty return head 
        if not head: return head
        
        counter=head
        count=1
        while counter.next:
            counter=counter.next
            count+=1
            
        if count==1 or count==k or k%count==0:
            return head
        k=k%count
        
        counter.next=head

        steps=count-k
        temp=head
        for i in range(steps-1):
            temp=temp.next
            
        res=temp.next
        temp.next=None
        return (res)
        
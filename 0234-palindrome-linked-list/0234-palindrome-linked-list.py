# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # method1: traverse the list, at the same time, append the nodes in the stack, now when reached Null, traverse from start, start poping from the stack, and again  compare both nodes, if stack gets empty and traverse reach Null return True, else Return False.

        # temp=head
        # stack=[]
        # while temp:
        #     stack.append(temp.val)            
        #     temp=temp.next
        # # print(stack)
        # while head:
        #     if head.val!=stack.pop():
        #         return False
        #     head=head.next
        # return True
        
        # method 2: use floyds algo and reach the middle of linked list
        # then run another pointer from the slow and reverse the remaining list
        # now take prev pointer which will be used for traversing reverse list 
        # and also use head pointer from start
        # traverse both pointers while prev becomes null ie
        # prev- middle to end ie reverse order or middle to end
        # front - front to middle

        
#         slow,fast=head, head
#         while fast and fast.next:
#             fast=fast.next.next
#             slow=slow.next

#         # if list is odd, skip middle node and only compare left, right halfs
#         if fast: slow=slow.next
            
#         prev=None
#         front=head
        
#         while slow:
#             nex=slow.next
#             slow.next=prev
#             prev=slow
#             slow=nex
            
#         while prev:
#             if front.val!=prev.val:
#                 return False
#             front=front.next
#             prev=prev.next
#         return True
        
        
        # method 3 : similar to method 2
        # but we will reverse the front to middle at the same time of traversing slow
        # and prev pointer will denote reversed list from front to middle
        # while slow pointer has reached middle so will traverse from middle to end
        
        
        
        
        
        slow,fast=head, head
        
        front=head
        prev=None
        
        
        while fast and fast.next:
            fast=fast.next.next
            # slow=slow.next
            nex=slow.next
            slow.next=prev
            prev=slow
            slow=nex  
            
        # print(prev)
        # print(slow)
        
        # if list is odd, skip middle node and only compare left, right halfs

        if fast: slow=slow.next

        while slow:
            if slow.val!=prev.val:
                return False
            slow=slow.next
            prev=prev.next
        return True
            
            
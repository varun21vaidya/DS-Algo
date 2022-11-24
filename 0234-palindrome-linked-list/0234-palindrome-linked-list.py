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
        # then run another pointer from the start
        
        #method2: first get to middle then reverse list
        
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
        
        if fast: slow=slow.next

        while prev:
            if slow.val!=prev.val:
                return False
            slow=slow.next
            prev=prev.next
        return True
            
            
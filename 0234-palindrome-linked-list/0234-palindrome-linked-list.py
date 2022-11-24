# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #method2: traverse the list, at the same time, append the nodes in the stack, now when reached Null, traverse from start, start poping from the stack, and again  compare both nodes, if stack gets empty and traverse reach Null return True, else Return False.
        
        #method1: counta length of list, if even, reverse upto middle, compare both front side, and from middle to end
        
        temp=head
        stack=[]
        while temp:
            stack.append(temp.val)            
            temp=temp.next
        # print(stack)
        while head:
            if head.val!=stack.pop():
                return False
            head=head.next
        return True
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        global front
        front = head
        
        def helper(back):
            global front
            if not back:
                return True
            
            till_equal = helper(back.next)
            
            isEqual = (back.val == front.val)
            
            front = front.next
            
            return till_equal and isEqual
        
        return helper(head)
        
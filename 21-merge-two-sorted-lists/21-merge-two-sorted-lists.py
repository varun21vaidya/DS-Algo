# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def solver(list1,list2,newlist):
            if not list1:
                newlist.next=list2
                return
            elif not list2:
                newlist.next=list1
                return
            if list1.val<=list2.val:
                newlist.next=list1
                solver(list1.next,list2,newlist.next)
            else:
                newlist.next=list2
                solver(list1,list2.next,newlist.next)
            
        newlist=ListNode()
        solver(list1,list2,newlist)
        return newlist.next
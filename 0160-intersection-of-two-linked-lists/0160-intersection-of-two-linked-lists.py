# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Brute Force-2 loops (TLE) 
        
        # temp=headB
        # while headA:
        #     headB=temp
        #     while headB:
        #         if headA==headB:
        #             return headB
        #         else:
        #             headB=headB.next
        #     headA=headA.next
        # return None
        
        sett=set()
        while headA:
            sett.add(headA)
            headA=headA.next
        # print(sett)
        while headB:
            if headB in sett:
                return headB
            headB=headB.next
        
        return None
            
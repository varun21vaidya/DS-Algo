# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Brute Force-2 loops (TLE) 
        # O(n^2)
        
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
        
        # Method 2 - Hashset
        
        # Use hashset and store list1 nodes in sett
        # and again use traverse in list2 and lookup if 
        # node is present in sett, if its there return it
        # else return None
        
        # TC: O(n+m) SC: O(n)
    
#         sett=set()
#         while headA:
#             sett.add(headA)
#             headA=headA.next
#         # print(sett)
#         while headB:
#             if headB in sett:
#                 return headB
#             headB=headB.next
        
#         return None
    
        c1,c2=0,0
        temp1,temp2=headA,headB
        
        # get count of both nodes
        while headA:
            c1+=1
            headA=headA.next
        
        while headB:
            c2+=1
            headB=headB.next
        
        # print(c1,c2)
        
        # if count1>count 2 traverse temp1 to c1-c2
        # else traverse temp2 c2-c1
        if c1>c2:
            # print("list1 is longer")
            while c1>c2:
                temp1=temp1.next
                c1-=1
        else:
            # print("list2 is longer")
            while c2>c1:
                temp2=temp2.next
                c2-=1
                
        while temp1 and temp2:
            if temp1==temp2:
                # print("got the node")
                return temp1
            temp1=temp1.next
            temp2=temp2.next
        
        return None
        
            
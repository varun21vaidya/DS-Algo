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
    
         # method 3: DIFFERENCE METHOD (Required and efficient)
    
        # take the difference between length of nodes
        # traverse the longer list upto difference between them
        # now traverse both the lists at same time, and 
        # check if both nodes are same, return the node
        # if not return Null
        
        # TC: O(m+n) SC: O(1)
#         c1,c2=0,0
#         temp1,temp2=headA,headB
        
#         # get count of both nodes
#         while headA:
#             c1+=1
#             headA=headA.next
        
#         while headB:
#             c2+=1
#             headB=headB.next
        
#         # print(c1,c2)
    
#         # if count1>count 2 traverse temp1 to c1-c2
#         # else traverse temp2 c2-c1
#         if c1>c2:
#             # print("list1 is longer")
#             while c1>c2:
#                 temp1=temp1.next
#                 c1-=1
#         else:
#             # print("list2 is longer")
#             while c2>c1:
#                 temp2=temp2.next
#                 c2-=1
                
#         while temp1 and temp2:
#             if temp1==temp2:
#                 # print("got the node")
#                 return temp1
#             temp1=temp1.next
#             temp2=temp2.next
        
#         return None

        
        # method 4 : BEST APPROACH

        # differece method will work but takes too many differnt components
        # instead we can use same diff appraoch but with just 2 pointers
        # take 2 pointers at each heads and if one of them goes to Null 
        # reassign them to opposite head and reiterate
        # now other also may go to null and need to reiterate
        # now at one point both will be at same position
        # this is our intersecting node
        # if at any point both pointers become null, there is no intersection
        # hence return Null
        
        # TC: O(m+n) SC: O(1)
        
        p1=headA
        p2=headB
        while p1!=p2:
            p1=p1.next
            p2=p2.next
            
            
            if not p1 and not p2:
                return None
            
            if not p1:
                p1=headB
            
            if not p2:
                p2=headA
        
        return p1    
            
        
            
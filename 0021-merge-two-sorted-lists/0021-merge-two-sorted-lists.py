# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative with extra space
        
#         temp=newlist=ListNode()
#         while list1 and list2:
#             if list1.val>list2.val:
#                 newlist.next=list2
#                 list2=list2.next
#             else:
#                 newlist.next=list1
#                 list1= list1.next
#             newlist= newlist.next
            
#         newlist.next= list1 or list2
        
#         return temp.next
    
    
        # not worked
        
#         if not list1: return list2
#         if not list2: return list1
        
#         if list1.val>list2.val:
#             temp=ListNode(list1)
#             list1=list2
#             list2=temp
#         # print(list1,list2)  
        
#         res= ListNode(list1)
#         while list1 and list2:
#             pointer= ListNode(None)
#             while list1 and list1.val<=list2.val:
#                 pointer=list1
#                 list1=list1.next
            
#             pointer.next=list2
            
#             temp=ListNode(list1)
#             list1=list2
#             list2=temp
#         return res

        
        if not list1: return list2
        if not list2: return list1
        
        if list1.val<list2.val:
            list1.next= self.mergeTwoLists(list1.next,list2)
            return list1
        
        else:
            list2.next= self.mergeTwoLists(list2.next,list1)
            return list2
    
        
        
        
        
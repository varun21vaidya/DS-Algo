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

        
        # Recursive
        
#         to implement implace with recursion,
#         we will check base condtion ie
#         if no list 1 or list2 is present we return list2 and list1 respectively
    
#         now if list1 value is less than list2 value,
#         we will reference list1.next pointer to result of mergeTwoLists(list1.next,list2)
#         and when list2 value becomes greater we will swap it as list1 and list1 as list2
#         so that at every stage, a lower value will be list1
        
        if not list1: return list2
        if not list2: return list1
        
        if list1.val<list2.val:
            list1.next= self.mergeTwoLists(list1.next,list2)
            return list1
        
        else:
            list2.next= self.mergeTwoLists(list2.next,list1)
            return list2
    
        
        
        
        
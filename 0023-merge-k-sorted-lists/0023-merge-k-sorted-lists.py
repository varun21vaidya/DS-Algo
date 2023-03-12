# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def mergesort(arr):
#             if len(arr)<=1:
#                 return arr
#             mid= len(arr)//2
#             x= mergesort(arr[:mid])
#             y= mergesort(arr[mid:])

#             return merge(x,y)
        
#         def merge(arr1, arr2):
#             m=len(arr1)
#             n= len(arr2)
#             arr=[-1]*(m+n)
#             i,j,k=0,0,0
#             while i<m and j<n:
#                 if arr1[i]<=arr2[j]:
#                     arr[k]=arr1[i]
#                     i+=1
#                 else:
#                     arr[k]=arr2[j]
#                     j+=1
#                 k+=1
            
#             while j<n:
#                 arr[k]=arr2[j]
#                 j+=1
#                 k+=1
#             while i<m:
#                 arr[k]=arr1[i]
#                 i+=1
#                 k+=1
            
#             return arr
        
#         def lltoarr(lists):
#             res=[]
#             for i in lists:
#                 while i:
#                     res.append(i.val)
#                     i=i.next
#             res= mergesort(res)
#             return arrtoll(res)
        
#         def arrtoll(arr):
#             x= head= ListNode()
#             for i in arr:
#                 x.next=ListNode(i)
#                 x=x.next
#             return head.next
        
            
#         return lltoarr(lists)
        
    
    
        def mergesort(lists):
            if not lists: return None
            if len(lists)==1:
                return lists[0]
            mid= len(lists)//2
            x= mergesort(lists[:mid])
            y= mergesort(lists[mid:])

            return merge(x,y)
        
        def merge(ll1, ll2):
            if not ll1 or not ll2:
                return ll1 or ll2
            ll= head= ListNode()
            while ll1 and ll2:
                if ll1.val<ll2.val:
                    ll.next=ll1
                    ll1= ll1.next
                else:
                    ll.next=ll2
                    ll2= ll2.next
                ll=ll.next
            
            ll.next= ll1 or ll2
            
            return head.next
        
        return mergesort(lists)

        
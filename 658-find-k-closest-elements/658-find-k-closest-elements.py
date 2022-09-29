class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        

#         def binarysearch(arr, item):
#             low, high = 0, len(arr)-1
#             while low <= high:
#                 mid = low+(high-low)//2
#                 if arr[mid] == item:
#                     return mid
#                 elif item > arr[mid]:
#                     low = mid+1
#                 else:
#                     high = mid-1
#             return -1

#         ind=binarysearch(arr, x)
#         print(ind)
#         if ind==-1:
#             lst=[]
#         else:
#             lst = [x]
#         i, j = 1, 1
#         while len(lst) < k:
#             print(lst)
#             if (arr[ind+i]-arr[ind]) < (arr[ind]-arr[ind-j]):
#                 lst.append(arr[ind+i])
#                 if (ind+i) < len(arr):
#                     i += 1
#             else:
#                 lst.append(arr[ind-j])
#                 if (ind-j) > 0:
#                     j += 1
#         return sorted(lst)

        low,high=0,len(arr)-k
        while low<high:
            mid=low+(high-low)//2
            if (x-arr[mid])>(arr[mid+k]-x):
                low=mid+1
            else:
                high=mid
            
        return arr[low:low+k]
            
        
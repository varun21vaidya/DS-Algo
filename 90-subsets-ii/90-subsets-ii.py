class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         # # TC: O(n*2^n) SC: O(n) #due to search in res 
#         def helper(ind, arr, res, temp):
#             if ind >= len(arr):
#                 if temp not in res:
#                     res.append(temp[:])
#                 return
#             temp.append(arr[ind])
#             helper(ind+1, arr, res, temp)
#             temp.pop()
#             helper(ind+1, arr, res, temp)

#         ind, res, temp = 0, [], []
#         nums.sort()
#         helper(ind, nums, res, temp)
#         return res

#         def helper(ind, arr, res, temp):
#             if ind >= len(arr):
#                 res.append(temp[:])
#                 return
            
#             for i in range(ind,len(arr)):
#                 if i>ind and arr[i]==arr[i-1]: continue
                    
#                 temp.append(arr[i])
#                 helper(ind+1, arr, res, temp)
#                 temp.pop()

#         ind, res, temp = 0, [], []
#         helper(ind, nums, res, temp)
#         return res



        # # TC: O(2^n) SC: O(n) 
        def helper(ind, arr, res, temp):
            if ind >= len(arr):
                res.add(tuple(temp[:]))
                return
            temp.append(arr[ind])
            helper(ind+1, arr, res, temp)
            temp.pop()
            helper(ind+1, arr, res, temp)

        ind, res, temp = 0, set(), []
        nums.sort()
        helper(ind, nums, res, temp)
        return res
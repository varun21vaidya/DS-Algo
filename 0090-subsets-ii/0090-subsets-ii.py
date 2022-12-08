class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def solver(arr,ind, temp):
            if ind>=n:
                res.add(tuple(temp))
                return
            temp.append(arr[ind])
            solver(arr,ind+1,temp)
            temp.pop()
            solver(arr,ind+1,temp)
            
        n=len(nums)
        res=set()
        nums.sort()
        solver(nums, 0, [])
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         # # TC: O(n*2^n) SC: O(n) #extra time for conversion to tuple
#         def helper(ind, arr, res, temp):
#             if ind >= len(arr):
#                 res.add(tuple(temp[:]))
#                 return
#             temp.append(arr[ind])
#             helper(ind+1, arr, res, temp)
#             temp.pop()
#             helper(ind+1, arr, res, temp)

#         ind, res, temp = 0, set(), []
#         nums.sort()
#         helper(ind, nums, res, temp)
#         return res
    
    
    
    
#         def helper(ind, temp):
#             # when recursion is called temp is added to resultant array
#             res.append(temp.copy())
            
#             for i in range(ind,len(nums)):
#                 if i!=ind and nums[i]==nums[i-1]: continue
                    
#                 temp.append(nums[i])
#                 helper(i+1,temp)
#                 temp.pop()

#         nums.sort()
#         ind, res, temp = 0, [], []
#         helper(ind, temp)
#         return res



    
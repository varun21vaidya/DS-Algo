class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
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
    
        def helper(ind, arr, res, temp):
            # when recursion is called temp is added to resultant array
            res.append(temp[:])
            
            for i in range(ind,len(arr)):
                if i!=ind and arr[i]==arr[i-1]: continue
                    
                temp.append(arr[i])
                helper(i+1, arr, res, temp)
                print(temp)
                temp.pop()

        nums.sort()
        ind, res, temp = 0, [], []
        helper(ind, nums, res, temp)
        return res



    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        #TLE
#         #iterations for candidates= ind
#         #temp array= arr
#         #resultant array= res
#         #temperory sum = temp
#         def helper(ind, arr, res, temp):
            
#             if ind==len(candidates):
#                 if temp==target:
#                     # print(arr, "added")
#                     res.add(tuple(sorted(arr[:])))
#                 return  
            
#             temp+=candidates[ind]
#             arr.append(candidates[ind])
#             helper(ind+1, arr, res, temp)
            
#             temp -= candidates[ind]
#             arr.pop()
#             helper(ind+1, arr, res, temp)
    
#         res=set()
#         helper(0, [], res, 0)
#         return res
                
    
        #TLE
#         #iterations for candidates= ind
#         #temp array= arr
#         #resultant array= res
#         def helper(ind, arr, target):
            
#             if ind==len(candidates):
#                 if target==0:
#                     # print(arr, "added")
#                     res.add(tuple(arr[:]))
#                 return  
            
#             if candidates[ind]<=target:
#                 arr.append(candidates[ind])
#                 helper(ind+1, arr, target-candidates[ind])
#                 arr.pop()
#             helper(ind+1, arr, target)

                
#         candidates.sort()
#         res=set()
#         helper(0, [], target)
#         return res
              
    
        def helper(ind, tempArr, target,res):
            
            if target==0:
                res.append(list(tempArr))
                return
            
            for i in range(ind, len(candidates)):
                
            # imp condition to avoid duplicates as for same numbers 
            # like 1 1 1 2 2, for recursion tree first 1 will start
            # when it moves it doesnot matter if its first one or second one
            # so only initial one is enough so it checks 
            # if i>ind ie its not first one and is same as previous one then skip it
            
                if (i>ind and candidates[i]==candidates[i-1]): continue
                    
                    
                    
                if candidates[i]>target: break
                    
                tempArr.append(candidates[i])
                helper(i+1, tempArr, target-candidates[i],res)
                tempArr.pop()
            
        candidates.sort()
        res=[]
        helper(0, [], target,res)
        return res
            
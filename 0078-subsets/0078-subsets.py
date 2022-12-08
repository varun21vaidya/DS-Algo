class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # TC: n*2^n
            
        n=len(nums)
#         res=[]
#         for i in range(1<<n):
#             temp=[]
            
#             for j in range(n):
#                 if i & 1<<j:
#                     temp.append(nums[j])
#             res.append(temp)
            
#         return res

        # Recursion
        n=len(nums) 
        def solver(arr,ind,temp):
            if ind>=n:
                res.append(temp.copy())
                return
            temp.append(arr[ind])
            solver(arr,ind+1,temp)
            temp.pop()
            solver(arr,ind+1, temp)
            
        res=[]
        solver(nums,0,[])
        return res
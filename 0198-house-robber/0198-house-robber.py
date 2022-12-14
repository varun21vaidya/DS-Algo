class Solution:
    def rob(self, nums: List[int]) -> int:
        
#         def robber(nums, go):
#             if go<0:
#                 return 0
            
#             return max(robber(nums, go-2)+nums[go] , robber(nums,go-1))
        
#         return robber(nums,len(nums)-1)
        
        
    
        def robber(nums, go):
            if go<0:
                return 0
            
            if memo[go]>=0:
                return memo[go]
            
            
            res= max(robber(nums, go-2)+nums[go] , robber(nums,go-1))
            memo[go]=res
            return res
        
        
        memo=[-1 for i in range(len(nums)+1)]
        return robber(nums,len(nums)-1)
            
        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
     
        totalsum,maxx=0,float('-inf')
        for i in range(len(nums)):
            totalsum+=nums[i]
            maxx=max(maxx,totalsum)

            if totalsum<0: totalsum=0
            
            
        return maxx
    
    
    
    
    
    
    
    
    
    
    
    
    
        
# #       brute force : (got TLE)
#         curr, maxx=0,float('-inf')
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 curr=sum(nums[i:j+1])
#                 maxx=max(maxx, curr)
#         return maxx
    
# #       Dynamic Programming - KADANE's Algorithm
#         curr=0
#         maxsum=float('-inf')
#         for i in nums:
#             curr+=i
#             if curr>maxsum:
#                 maxsum=curr
#             if curr<0:
#                 curr=0
#         return maxsum
        
#         currmax,maxx=0,nums[0]
#         for i in range(len(nums)):
#             currmax=max(nums[i], nums[i]+currmax)
#             maxx=max(maxx, currmax)
#         return maxx
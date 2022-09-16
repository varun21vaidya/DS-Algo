class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        
#       recursive solution (GOT TLE)

#         def f(mul,start,end):
#             if  mul == len(multipliers):
#                 return 0
            
            
#             recurse1=multipliers[mul]*nums[start]+f(mul+1,start+1,end)
#             recurse2=multipliers[mul]*nums[end]+f(mul+1,start,end-1)

#             return max(recurse1,recurse2)
        
#         return f(0,0,len(nums)-1)




#         # Use Memoization (DP) 
        
#         # To avoid TLE due to recursion we will use memoization as many of the recursions 
#         # will be repeated in the process, so use a dp array to store those values
        
#         dp=[[-1 for i in range(1001)] for j in range(1001)]
#         def f(mul,start):
#             if  mul == len(multipliers):
#                 return 0
            
#             # as every value is stored as -1, those who are not were already saved in dp
#             if dp[mul][start]!=-1:
#                 return dp[mul][start]
            
            
#         # to reduce complexity we can calulate end manually
#         # from how much indexes are covered ie mul and how much of them were from start
#         # now difference between them will give total numbers used from end 
#         # and subtracting from len will give current end index 

#             end=len(nums)-(mul-start)-1

#             recurse1=multipliers[mul]*nums[start]+f(mul+1,start+1)
#             recurse2=multipliers[mul]*nums[end]+f(mul+1,start)
            
#             #store the max possibilities in dp array and return 
#             dp[mul][start]=max(recurse1,recurse2)
#             return dp[mul][start]
        
#         return f(0,0)
        
        ## STILL GOT TLE
        
        
        
        
        
#         #Now use dictionary to store dp values
#         dp={}
#         def f(mul,start):
#             if  mul == len(multipliers):
#                 return 0
            
            
#             if (mul,start) in dp:
#                 return dp[(mul,start)]  
        
#             end=len(nums)-(mul-start)-1
#             recurse1=multipliers[mul]*nums[start]+f(mul+1,start+1)
#             recurse2=multipliers[mul]*nums[end]+f(mul+1,start)
            
#             #store the max possibilities in dp array and return 
#             dp[(mul,start)]=max(recurse1,recurse2)
#             return dp[(mul,start)]
        
#         return f(0,0)


        # # STILLL GOT TLE
    
    
    
    
    
    
    
    
    
    
        # #USE LRU CACHE
        
#         @lru_cache(None)
#         def f(mul,start):
            
#             if  mul == len(multipliers):
#                 return 0 

#             end=len(nums)-(mul-start)-1
#             recurse1=multipliers[mul]*nums[start]+f(mul+1,start+1)
#             recurse2=multipliers[mul]*nums[end]+f(mul+1,start)

            
#             return max(recurse1,recurse2)
           

#         ans=f(0,0)
#         f.cache_clear()
#         return ans
    
    ## STILLLLLL GOT TLE
    
    
    
        n, m = len(nums), len(multipliers)
        dp = [[0 for _ in range(m + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - i + left
                dp[i][left] = max(multipliers[i] * nums[left] + dp[i + 1][left + 1], 
                                  multipliers[i] * nums[right] + dp[i + 1][left])

        return dp[0][0]
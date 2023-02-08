class Solution:
    def jump(self, nums: List[int]) -> int:
#         mapp={}
#         @lru_cache()
#         def helper(index=0):
#             ans=float('inf')
#             if index>=len(nums)-1:
#                 return 0
#             if index in mapp:
#                 return mapp[index]
#             for i in range(index, index+nums[index]):
#                 ans=min(ans,1+helper(i+1))
#             mapp[index]=ans    
#             return ans
        
#         index=0
#         return helper(index)
    
        # Greedy
        l,r,steps=0,0,0
        while r<len(nums)-1:
            maxxdist=0
            for i in range(l, r+1):
                maxxdist=max(maxxdist, i+nums[i])
            
            l=r+1
            r=maxxdist
            steps+=1
        
        return steps
            
        

#         n = len(nums)
#         jumps = [n] * n
#         jumps[0] = 0
#         for i in range(n):
#             for j in range(i + 1, min(i + nums[i] + 1, n)):
#                 jumps[j] = min(jumps[j], jumps[i] + 1)
#         return jumps[n - 1]
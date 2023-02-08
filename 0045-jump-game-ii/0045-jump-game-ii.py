class Solution:
    def jump(self, nums: List[int]) -> int:
        mapp={}
        def helper(index=0):
            ans=float('inf')
            if index>=len(nums)-1:
                return 0
            if index in mapp:
                return mapp[index]
            for i in range(index, index+nums[index]):
                ans=min(ans,1+helper(i+1))
            mapp[index]=ans    
            return ans
        
        index=0
        return helper(index)
    
        # # greedy
        # i,n=0, len(nums)-1
        # steps=0
        # while i<=n:
        #     if i==n:
        #         return steps
        #     steps+=1
        #     maxx=-1
        #     ind=0
        #     for j in range(1,nums[i]+1):
        #         if i+j==n:
        #             return steps
        #         if maxx<nums[i+j]:
        #             maxx=nums[i+j]
        #             ind=j
        #     i=i+ind
        





        # recursive
        # n=len(nums)
        # @lru_cache()
        # def solver(curr,steps,minsteps):
        #     if curr>=n:
        #         return minsteps
            
        #     if curr==n-1:
        #         minsteps=min(steps,minsteps)
        #         return minsteps
            
        #     for i in range(1, nums[curr]+1):
        #         minsteps=solver(curr+i, steps+1,minsteps)

        #     return minsteps
    
    
        # return solver(0,0,n+1)




#         n = len(nums)
#         jumps = [n] * n
#         jumps[0] = 0
#         for i in range(n):
#             for j in range(i + 1, min(i + nums[i] + 1, n)):
#                 jumps[j] = min(jumps[j], jumps[i] + 1)
#         return jumps[n - 1]
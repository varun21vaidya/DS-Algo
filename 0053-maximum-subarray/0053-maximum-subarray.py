class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
#       brute force : (got TLE)
        # curr, maxx=0,float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         maxx=max(maxx, sum(nums[i:j+1]))
        # return maxx
    
#       Dynamic Programming - KADANE's Algorithm
        # curr=0
        # maxsum=float('-inf')
        # for i in nums:
        #     curr+=i
        #     if curr<0:
        #         curr=0
        #     elif curr>maxsum:
        #         maxsum=curr
        # return maxsum
        
        currmax,maxx=0,nums[0]
        for i in range(len(nums)):
            currmax=max(nums[i], nums[i]+currmax)
            maxx=max(maxx, currmax)
        return maxx
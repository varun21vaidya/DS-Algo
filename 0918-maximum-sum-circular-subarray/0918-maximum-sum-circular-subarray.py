class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalsum=0
        maxsum,currmaxx=0,nums[0]
        minsum,currminn=0,nums[0]
        for el in nums:
            maxsum=max(el,maxsum+el)
            currmaxx=max(maxsum,currmaxx)
            
            minsum=min(el,minsum+el)
            currminn=min(minsum,currminn)
            
            totalsum+=el
            
        if currmaxx>0:
            return max(currmaxx,totalsum-currminn)
        else:
            return currmaxx

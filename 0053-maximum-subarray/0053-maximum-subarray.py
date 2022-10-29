class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        maxsum=float('-inf')
        for i in nums:
            curr+=i
            if curr>maxsum:
                maxsum=curr
            if curr<0:
                curr=0
        return maxsum
        
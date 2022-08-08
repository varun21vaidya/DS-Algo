class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        #dp solution
        # first iterate over each number and then
        # we will get tab for each number with ending as that number only
        # ie it is highest number in that list
        # and with each iteration of loop it will consider highest numbered list
        # which has last element smaller than our current element
        # and at the end we will get list with most numbers in increasing order
        
        n=len(nums)
        dp=[1]*n
        
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
        
        return max(dp)
        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
#         #dp solution (n^2 Solution)
#         # first iterate over each number and then
#         # we will get tab for each number with ending as that number only
#         # ie it is highest number in that list
#         # and with each iteration of loop it will consider highest numbered list
#         # which has last element smaller than our current element
#         # and at the end we will get list with most numbers in increasing order
        
#         n=len(nums)
#         dp=[1]*n
        
#         for i in range(n):
#             for j in range(i):
#                 if nums[i]>nums[j] and dp[i]<dp[j]+1:
#                     dp[i]=dp[j]+1
        
#         return max(dp)
    
    
    
#     n log(n) Solution
#     bisect is based on binary search 
#     where it returns an index of left most priority where the number given can be placed
#     here we will maintain a subarray of increasing sequence
#     if any value greater than its last value appears append it to last
#     else assume that the value is in range of already present numbers and it can be used
#     to further continue the array to increase subsequence
#     so put that number to smallest number greater than it
#     ie its closest bigger number
#     and as we modify the list it will give as final list as longest subsequence
    
        sub=[]
        for i in nums:
            if len(sub)==0 or sub[-1]<i:
                sub.append(i)
            else:
                ind= bisect_left(sub,i)
                sub[ind]=i
            
        return len(sub)
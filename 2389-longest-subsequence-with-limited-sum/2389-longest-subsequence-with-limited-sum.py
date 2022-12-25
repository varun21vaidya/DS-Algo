class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         nums.sort()
#         ans=[]
#         for que in queries:
#             add, size= 0,0
#             for i in nums:
#                 if add+i<=que:
#                     add+=i
#                     size+=1
#                 else:
#                     break
#             ans.append(size)

#         return ans

        nums.sort()
        ans=[]
        
        # print(nums)
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        # print(nums)
        
        for query in queries:
            ind= bisect.bisect_right(nums,query)
            ans.append(ind)
            
        return ans
            
            
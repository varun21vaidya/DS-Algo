class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
#         nums.sort()
#         if not nums: return 0
#         maxx,temp=1,1
#         for i in range(1,len(nums)):
#             # print(nums[i],maxx,temp)
#             if nums[i]==nums[i-1]+1:
#                 temp+=1
#             # if number same as previous num, ignore it
#             elif nums[i]!=nums[i-1]:
#                 temp=1
#             maxx=max(maxx,temp)
#         return (maxx)
    
    # first append all elements to set
    # use while loop to check if i-1 is present and update curr and maxx
    # return maxx
        # hashset=set(nums)
        # if not nums: return 0
        # maxx=0
        # for i in hashset:
        #     temp=1
        #     while i-1 in hashset:
        #         temp+=1
        #         i=i-1
        #     maxx=max(temp,maxx)
        # return maxx
    
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
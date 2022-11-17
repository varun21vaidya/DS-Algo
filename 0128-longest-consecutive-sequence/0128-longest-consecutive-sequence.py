class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums: return 0
        maxx,temp=1,1
        for i in range(1,len(nums)):
            print(nums[i],maxx,temp)
            if nums[i]==nums[i-1]+1:
                temp+=1
            # if number same as previous num, ignore it
            elif nums[i]!=nums[i-1]:
                temp=1
            maxx=max(maxx,temp)
        return (maxx)
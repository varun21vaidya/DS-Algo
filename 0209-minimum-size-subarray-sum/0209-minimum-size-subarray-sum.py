class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lst=[0]
        for i in range(1,len(nums)+1):
            lst.append(lst[i-1]+nums[i-1])
        # print(lst)
        # sliding window:
        low,high=1,1
        mini=len(lst)+1
        while high<len(lst):
            while lst[high]-lst[low-1]>=target:
                mini=min(mini,high-low+1)
                low+=1
            high+=1
        # print(mini)
        if mini>len(lst):
            return 0
        return mini

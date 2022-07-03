class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        n=len(nums)
        if n<2:return 1
        if n==2:
            if nums[0]!=nums[1]:return 2
            else:return 1
        
        last,length=2,1
        for i in range(1,n):
            if nums[i]==nums[i-1]:continue
            
            diff=nums[i]>nums[i-1]
            if last!=diff:
                last=diff
                length+=1
            
        return length
            
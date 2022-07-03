class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
#        if only 1 element return 1
#       if only 2 element and if both diff then 2 ..else 1

        n=len(nums)
        if n<2:return 1
        if n==2:
            if nums[0]!=nums[1]:return 2
            else:return 1
        
        
#       last is like a flag which checks 
#       if last element diff is opposite sign of current element diff
#       ie for each diff it assumes True or False
#       True, if current element greater than previous else false

        last,length=2,1
        
        for i in range(1,n):
            if nums[i]==nums[i-1]:continue
            
            diff=nums[i]>nums[i-1]
            if last!=diff:
                last=diff
                length+=1
            
        return length
            
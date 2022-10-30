class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort
        red=nums.count(0)
        white= nums.count(1)
        for i in range(len(nums)):
            if red>0:
                red-=1
                nums[i]=0
            elif white>0:
                white-=1
                nums[i]=1
            else:
                nums[i]=2
                
            
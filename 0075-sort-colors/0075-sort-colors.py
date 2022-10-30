class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # counting sort (2 passes)
        red,white=0,0
        for i in nums:
            if i==0: red+=1
            elif i==1: white+=1
                
        for i in range(len(nums)):
            if red>0:
                red-=1
                nums[i]=0
            elif white>0:
                white-=1
                nums[i]=1
            else:
                nums[i]=2
                
        
                
            
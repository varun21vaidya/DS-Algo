class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        res=0
        
#       a triangle should not have any length longer than sum of other lengths
        for i in range(len(nums)-2):
            print(nums[i],nums[i+1],nums[i+2])
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
            
        return 0
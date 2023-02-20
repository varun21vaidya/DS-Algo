class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binary_search(nums,target):
            n=len(nums)
            i,j=0,n
            while i<j:
                mid= i+ (j-i)//2
                if nums[mid]>=target:
                    j=mid
                else:
                    i=mid+1
            return i
    
        return binary_search(nums,target)
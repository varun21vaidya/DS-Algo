class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#   so to calculate first and last occurance of element in sorted array
#   we need to do binary search which will result in O(n)

#   but how to do it with repeated values
#   key is to use it twice, 1st for starting and 2nd for ending position

        starting =-1
        l,h,=0,len(nums)-1
        
        while l<=h:
            mid = l+ (h-l)//2
            
            if nums[mid]>target:
                h=mid-1
                
                
            elif nums[mid]==target:
                starting = mid
                h= mid-1
                
            elif nums[mid]<target:
               l= mid+1 
                
        # print(starting)
        
        ending =-1
        l,h,=0,len(nums)-1
        
        while l<=h:
            mid = l+ (h-l)//2
            
            if nums[mid]<target:
                l= mid+1
                
            elif nums[mid]==target:
                ending = mid
                l= mid+1
                
            else:
                h=mid-1
        # print(ending)
        
        
        return [starting, ending]
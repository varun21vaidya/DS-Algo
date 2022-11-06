class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        def binary_search(nums, target):
            l,r=0,len(nums)-1
            while l<r:
                mid=l+(r-l)//2
                if nums[mid]<target:
                    l=mid+1
                else:
                    r=mid
            return True if target==nums[l] else False
        
        x= [i for row in matrix for i in row]
        print(x)
        if len(x)==1: return target==x[0]
        return binary_search(x,target)
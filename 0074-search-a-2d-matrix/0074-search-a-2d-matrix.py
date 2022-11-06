class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
#         def binary_search(nums, target):
#             l,r=0,len(nums)-1
#             while l<r:
#                 mid=l+(r-l)//2
#                 if nums[mid]<target:
#                     l=mid+1
#                 else:
#                     r=mid
#             return True if target==nums[l] else False
        
# #       Brute Force O(n^2)- to convert 2d matrix to 1d matrix
#         # x= [i for row in matrix for i in row]
#         # # print(x)
#         # return binary_search(x,target)
    
#         
        m,n=len(matrix),len(matrix[0])
        low,high=0,m*n-1
        while low<=high:
            mid=low+(high-low)//2
            if matrix[mid//n][mid%n]==target:
                return True
            elif matrix[mid//n][mid%n]<target:
                low=mid+1
            else:
                high=mid-1
        return False
                
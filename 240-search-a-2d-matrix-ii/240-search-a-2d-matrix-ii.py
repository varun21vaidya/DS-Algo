class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(lst,target):
            l,h=0, len(lst)-1
            while l<h:
                mid = l+ (h-l)//2
                if lst[mid]<target:
                    l=mid+1
                else:
                    h=mid
            return lst[l]==target
        
        
#         go from bottom to top to check if first column has value less than target
            
        for i in range(len(matrix)-1, -1,-1):
            if matrix[i][0]<=target:
                if binary_search(matrix[i],target):
                    return True
        return False
                 
                
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        row,col=0,n-1
        def recurse(row,col):
            
            if row>=m or col<0: return False
            ele=matrix[row][col]
            if target==ele: return True
            elif target>ele:
                return recurse(row+1,col)
            else:
                return recurse(row,col-1)
        return recurse(row,col)
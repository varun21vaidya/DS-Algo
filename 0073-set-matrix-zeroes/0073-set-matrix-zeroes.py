class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        # TC: O(m*n) SC: O(m+n)
        
#       traverse through matrix and if the ele is zero store its row and col in saperate arrays
#       and traverse through that stored row array and make those rows zeros.
#       traverse through all rows and thorough stored col array and make those cols zeros

#       function to make entire row zero

        def setrows(setzerorow):
            for i in setzerorow:
                matrix[i]=[0]*cols
                
#       function to make entire column zero

        def setcols(setzerocol):
            for i in range(rows):
                for j in setzerocol:
                    matrix[i][j]=0
                    
                    
        rows, cols= len(matrix), len(matrix[0])
        setzerorow,setzerocol=[],[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    setzerorow.append(i)
                    setzerocol.append(j)
                    
        setrows(setzerorow)
        setcols(setzerocol)
        
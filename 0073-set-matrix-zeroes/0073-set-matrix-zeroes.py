class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setrows(setzerorow):
            for i in setzerorow:
                matrix[i]=[0]*cols
        
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
        
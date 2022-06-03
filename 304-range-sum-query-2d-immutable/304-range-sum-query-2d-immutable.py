class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix), len(matrix[0])
        self.newmat=[[0]*(col+1) for i in range(row+1)]
        for i in range(row):
            prefix=0
            for j in range(col):
                prefix+=matrix[i][j]
                above=self.newmat[i][j+1]
                self.newmat[i+1][j+1]=prefix+above
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        bottomright=self.newmat[row2+1][col2+1]
        top=self.newmat[row1][col2+1]
        left=self.newmat[row2+1][col1]
        topleft=self.newmat[row1][col1]
        
        return bottomright-top-left+topleft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
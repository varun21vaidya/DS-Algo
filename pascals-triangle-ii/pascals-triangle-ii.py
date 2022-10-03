class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        main=[[1]]
        for i in range(1,rowIndex+1):
            temp=[1]*(i+1)
            main.append(temp)
            for j in range(1,i):
                main[i][j]=main[i-1][j-1]+main[i-1][j]
                
        return main[rowIndex]
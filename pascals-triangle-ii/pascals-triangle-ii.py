class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
#         main=[[1]]
#         for i in range(1,rowIndex+1):
#             temp=[1]*(i+1)
#             main.append(temp)
#             for j in range(1,i):
#                 main[i][j]=main[i-1][j-1]+main[i-1][j]
                
#         return main[rowIndex]

        def getPascal(row,dp):

            if row==1:
                dp.append([1])
                return dp

            getPascal(row-1,dp)
            new=[1]
            for i in range(len(dp[-1])-1):
                new.append(dp[-1][i]+dp[-1][i+1])
            new.append(1)  
            dp.append(new)
            return dp
        
        return getPascal(rowIndex+1,[])[-1]
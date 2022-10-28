class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        
#         Iterative Approach:
        
#         res=[[1]]
#         if numRows==1:
#             return res
#         res.append([1,1])
#         if numRows==2:
#             return res
        
#         for i in range(2,numRows):
#             temp=[1]*(i+1)
#             for j in range(1,i):
#                 temp[j]=res[i-1][j-1]+res[i-1][j]
#             res.append(temp)
#         return res

        # recursive approach
    
        if numRows==1:
            return [[1]]
        prev=self.generate(numRows-1)
        last_row=prev[-1]
        
        new_row=[1]
        for i in range(1,len(last_row)):
            new_row.append(last_row[i-1]+last_row[i])
        new_row.append(1)
        
        return prev+[new_row]
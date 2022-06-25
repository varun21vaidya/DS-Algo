class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle)==0:
            return
        res=[[0 for i in range(len(row))]for row in triangle]
        res[0][0]=triangle[0][0]
        print(res)
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    res[i][j]=res[i-1][j]+triangle[i][j]
                elif j==len(triangle[i])-1:
                    res[i][j]=res[i-1][j-1]+triangle[i][j]
                else:
                    res[i][j]=min(res[i-1][j-1],res[i-1][j])+triangle[i][j]
                    
                
        return min(res[-1])
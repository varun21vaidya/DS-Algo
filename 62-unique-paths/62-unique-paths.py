class Solution:
    def uniquePaths(self, m, n,i=0, j=0):
        # def countpaths(m,n,i,j):
        #     if (i>=m or j>=n): return 0
        #     if (i==m-1 or j==n-1): return 1
        #     else:
        #         return countpaths(m,n,i+1,j) + countpaths(m,n,i,j+1)
        # return countpaths(m,n,0,0)
        
        
        dp=[[-1 for i in range(n)] for i in range(m)]
        # print(dp)
        def countpaths(m,n,i,j):
            if (i>=m or j>=n): return 0
            if (i==m-1 or j==n-1): return 1
            if dp[i][j]!=-1: return dp[i][j]
            else:
                dp[i][j]=countpaths(m,n,i+1,j) + countpaths(m,n,i,j+1)
                return dp[i][j]
        return countpaths(m,n,0,0)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # ITERATIVE DP SOLUTION:
        
#       as for certain i,j it can reach either from top or left
#       so the border of top and left will have only 1 way to reach
#       so make a dp grid of number of ways to reach at certain point
#       and for the point add the ways from top and left

        # dp=[[0 for i in range(n)] for j in range(m)]
#       # print(dp)
        # for i in range(m):
        #     for j in range(n):
        #         if i==0 or j==0:
        #             dp[i][j]=1
        #         else:
        #             dp[i][j]=dp[i-1][j]+dp[i][j-1]
        # # print(dp)
        # return dp[m-1][n-1]
        
        
#       RECURSIVE SOLUTION TOP DOWN
        @lru_cache(maxsize=None)
        def help(i,j,m,n):
            if i>=m or j>=n:
                return 0
            elif i==m-1 and j==n-1:
                return 1
            else:
                return help(i+1,j,m,n)+help(i,j+1,m,n)
        
        return help(0,0,m,n)

#      
        def help(i,j,m,n,dp):
            if i>=m or j>=n:
                return 0
            elif i==m-1 and j==n-1:
                return 1
            else:
                if (i,j) in dp:
                    return dp[(i,j)]
                
                dp[(i,j)]= help(i+1,j,m,n,dp)+help(i,j+1,m,n,dp)
                return dp[(i,j)]
        
        dp={}
        return help(0,0,m,n,dp)

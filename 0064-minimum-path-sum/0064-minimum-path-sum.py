from collections import defaultdict
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
#         m=len(grid)
#         n=len(grid[0])
        
#         def solver(x,y,summ):
#             nonlocal ans
            
#             if x>=m or y>=n or x<0 or y<0:
#                 return 0
            
#             summ+=grid[x][y]
            
#             if x==m-1 and y==n-1:
#                 if ans==0:
#                     ans=summ
#                 elif summ>0:
#                     if summ<ans:
#                         ans=summ
#                 return ans
            
#             solver(x+1,y,summ)
#             solver(x,y+1,summ)
            
#             return ans
        
#         ans=0
#         solver(0,0,0)
#         return ans
                
    
        m=len(grid)
        n=len(grid[0])

        def solver(x,y,summ):

            if x>=m or y>=n or x<0 or y<0:
                return float('inf')

            if x==m-1 and y==n-1:
                return grid[x][y]

            if dp[x][y]!=-1:
                return dp[x][y]


            dp[x][y]=grid[x][y]+ min(solver(x+1,y,summ),solver(x,y+1,summ))

            return dp[x][y]


        if m==1 and n==1:
            return grid[0][0]
        dp=[[-1]*(n) for i in range(m)]
        solver(0,0,0)
        return dp[0][0]
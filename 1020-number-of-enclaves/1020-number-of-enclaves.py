class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j):
            drow=[-1,0,1,0]
            dcol=[0, 1, 0, -1]
            m=len(grid)
            n=len(grid[0]) 
            
            if i<0 or j<0 or i>=m or j>=n or not grid[i][j] or (i,j) in vis:
                return 0
            
            vis.add((i,j))
            borderside=1
            
            for d in range(4):
                row,col = i+ drow[d], j+ dcol[d]
                
                if (row>=0 and col>=0 and row<m and col<n ) and grid[row][col] and (row,col) not in vis:
                    borderside+=dfs(row,col)
                    
            return borderside
        
        m=len(grid)
        n=len(grid[0])
        count,borderlands=0,0
        vis=set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count+=1
                    if (i==0 or j==0 or i==m-1 or j==n-1) and (i,j) not in vis:        
                        borderlands+= dfs(i,j)
        
        return count-borderlands
                    
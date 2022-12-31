class Solution:
    def uniquePathsIII(self, grid):
        
        
        self.res = 0
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                if grid[i][j] == 0:
                    empty += 1

        def dfs(x, y, empty):
            
            if (0 > x or x >= m or 0 > y or y>= n or grid[x][y] < 0): return
            
            if grid[x][y] == 2:
                if empty==0:
                    self.res += 1
                return
            
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
        dfs(x, y, empty)
        return self.res
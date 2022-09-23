class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowlen,collen= len(grid), len(grid[0])
        visited=set()
        def dfs(r,c):
            # first remove those elements which are out of bound
            # or not island or have been already visited
            if (r<0 or  r==rowlen or c<0 or c==collen or grid[r][c]==0 or (r,c) in visited):
                return 0
            
            #then as its island then add it to visited set
            visited.add((r,c))
            
            #and add the others from all 4 its neighbouring directions
            return (1+ dfs(r+1,c)+dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1))
        
        #now iterate for every row column and calculate max area
        area=0    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area=max(area, dfs(r,c))
        
        return area
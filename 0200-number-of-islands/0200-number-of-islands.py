class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(i,j,vis):
            dirrow=[-1,0,1,0]
            dircol=[0,1,0,-1]
            vis.add((i,j))
            q=deque([])
            q.append((i,j))
            
            m=len(grid)
            n=len(grid[0])
            while q:
                i,j = q.popleft()
                for d in range(4):
                    row,col=dirrow[d]+i, dircol[d]+j
                    if row>=0 and row<m and col>=0 and col<n and grid[row][col]=="1" and (row,col) not in vis:
                        vis.add((row,col))
                        q.append((row,col))
            
        
        vis=set()
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in vis:
                        bfs(i,j,vis)
                        count+=1
        return count
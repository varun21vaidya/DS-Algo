#User function Template for python3

from typing import List
from collections import deque

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
    
        # we need to find 1s that are not on boundry
        # so we find total 1s and subtract ones that are on boundry
        
        m=len(grid)
        n=len(grid[0])
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        vis=set()
        q=deque()
        oneCount=0
        
        # gives tle for last 2 test cases
        def dfs(i,j,vis):
            vis.add((i,j))
            
            for d in range(4):
                row,col=drow[d]+i, dcol[d]+j
                
                if row>=0 and row<m and col>=0 and col<n and (row,col) not in vis and grid[row][col]==1:
                    dfs(row,col,vis)
                
        def bfs(i,j,vis):
            vis.add((i,j))
            
            while q:
                r,c = q.popleft()
                
                for d in range(4):
                    row,col=drow[d]+r, dcol[d]+c
                    
                    if row>=0 and row<m and col>=0 and col<n and (row,col) not in vis and grid[row][col]==1:
                        q.append((row,col))
                        vis.add((row,col))
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    oneCount+=1
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        q.append((i,j))
                        vis.add((i,j))
                        # bfs(i,j,vis)
        while q:
            r,c = q.popleft()
            
            for d in range(4):
                row,col=drow[d]+r, dcol[d]+c
                
                if row>=0 and row<m and col>=0 and col<n and (row,col) not in vis and grid[row][col]==1:
                    q.append((row,col))
                    vis.add((row,col))

        return oneCount-len(vis)
                    
                
                    
                        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends
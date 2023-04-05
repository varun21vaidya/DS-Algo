#User function Template for python3

import sys
sys.setrecursionlimit(10**8)
from collections import deque
class Solution:
    def numIslands(self,grid):
        def bfs(i,j):
            vis.add((i,j))
            q=deque([])
            q.append((i,j))

            drow=[-1,-1,0,1,1,1,0,-1]
            dcol=[0,1, 1,1,0,-1,-1,-1]
            m=len(grid)
            n=len(grid[0])
            
            while q:
                i,j = q.popleft() # O(1)

                for d in range(8):
                    row,col= i+drow[d], j+dcol[d]
                    
                    if row>=0 and row<m and col>=0 and col<n:
                        if (row,col) not in vis and grid[row][col]==1:
                            q.append((row,col))
                            vis.add((row,col))

            # print(vis)

        m=len(grid)
        n=len(grid[0])
        vis=set() # visited set
        count=0 # number of islands
        for i in range(m):
            for j in range(n):
                if (i,j) not in vis and grid[i][j]==1:
                    bfs(i,j)
                    count+=1
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends
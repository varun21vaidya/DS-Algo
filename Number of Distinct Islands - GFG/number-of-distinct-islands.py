#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)
from collections import defaultdict
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        
        def dfs(i,j,temp,basei,basej):

            vis.add((i,j))
            temp.append((basei-i, basej-j))

            drow=[-1,0,1,0]
            dcol=[0,1,0,-1]
            m=len(grid)
            n=len(grid[0])

            for d in range(4):
                row,col= i+drow[d], j+dcol[d]

                if row>=0 and row<m and col<n and col>=0:
                    if grid[row][col]==1 and (row,col) not in vis:
                        dfs(row,col,temp,basei,basej)
            

    
        vis=set()
        m=len(grid)
        n=len(grid[0])
        count=0
        distinct=set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in vis:
                    temp=[]
                    dfs(i,j,temp,i,j)
                    distinct.add(tuple(temp))
                    count+=1

        return len(distinct)
        
        # def dfs(i,j,srcrow,srccol,store):
        #     m=len(grid)
        #     n=len(grid[0])
        #     vis.add((i,j))
        #     store.append((i-srcrow,j-srccol))
        #     drow=[-1,0,1,0]
        #     dcol=[0, 1, 0, -1]
            
        #     for d in range(4):
        #         row,col=drow[d]+i, dcol[d]+j

        #         if row>=0 and row<m and col>=0 and col<n:
        #             if grid[row][col]==1 and (row,col) not in vis:
        #                 vis.add((row,col))
                        
        #                 dfs(row,col,srcrow,srccol,store)
            
        # vis=set()  
        # res=[]
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if (i,j) not in vis and grid[i][j]==1:
        #             store=[]
        #             dfs(i,j,i,j,store)
        #             res.append(store)
        
        # # print(res)
        # ans=set()
        # for lst in res:
        #     ans.add(tuple(lst))
        
        # return len(ans)
        
            


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
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends
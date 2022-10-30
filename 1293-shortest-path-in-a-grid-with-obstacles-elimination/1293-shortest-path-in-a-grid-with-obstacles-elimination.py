class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
#         # define m,n, directions, dp arry, queue, steps
#         m,n=len(grid),len(grid[0])
#         dirn=[[0,0],[0,1],[1,0],[1,1]]
#         dp={}
#         q= [[0,0,k]]
#         heapq.heapify(q)
#         steps=0
        
#         # start bfs until q is empty, define size, pop ele from q to curr
#         while q:
#             size=len(q)
#             while size-1>0:
#                 size-=1
#                 curr=heapq.heappop(q)
                
#                 # if curr reach to destination, return steps
                
#                 if curr[0]==m-1 and curr[1]==n-1:
#                     return steps
                
#                 # loop through directions, define i,j,obs:
#                 for d in dirn:
#                     i=curr[0]+d[0]
#                     j=curr[1]+d[1]
#                     obs=curr[2]
                    
#                     # traverse through valid cells           
#                     if i>=0 and j>=0 and i<m and j<n:
                        
#                         # if cell is empty visit cell, add to queue and dp array
#                         if grid[i][j]==0 and not (i,j,obs) in dp:
                            
#                             heapq.heappush(q,[i,j,obs])
#                             dp[(i,j,obs)]=True
                            
#                         # else reduce obs, add to queue and dp array
#                         elif grid[i][j]==1 and obs>0 and not (i,j,obs) in dp:
#                             heapq.heappush(q,[i,j,obs-1])
#                             dp[(i,j,obs)]=True
                            
#             steps+=1
#         return -1

        m, n = len(grid), len(grid[0])
        # [1] this check significantly improves runtime, i.e.,
        #    we can use path (0,0) -> (0,n-1) -> (m-1,n-1)
        if k >= m + n - 2: return m + n - 2
       
        # [2] we use deque to store and update a BFS state that is
        #    (x, y, obstacles we can destroy, steps done so far)
        dq = deque([(0, 0, k, 0)])
        # [3] we also keep track of visited cells
        seen = set()
        
        while dq:
            i, j, k, s = dq.popleft()
            # [4] successfully reached lower right corner
            if (i,j) == (m-1,n-1) : return s
            
            # [5] scan all possible directions
            for ii, jj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                # [6] check boundaries and obstacles
                if 0 <= ii < m and 0 <= jj < n and k >= grid[ii][jj]:
                    # [7] make (and remember) a step
                    step = (ii, jj, k-grid[ii][jj], s+1)
                    if step[0:3] not in seen:
                        seen.add(step[0:3])
                        dq.append(step)
        
        # [8] failed to reach lower right corner
        return -1
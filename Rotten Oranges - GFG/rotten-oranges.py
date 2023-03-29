from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
        time =0
        m=len(grid)
        n=len(grid[0])
        q=deque([])
        vis=dict()
        countFresh=0
        mat=grid[:]
        
        # directions array, top, right, bottom , left
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        
        # first traverse the matrix and find the rotten oranges
        # and add them to que and visited
        # also we we find any empty spaces, add them to visited dictionary 
        # also keep a counter for fresh oranges, so at last we can check if any fresh ones are remained
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([(i,j),time])
                    vis[(i,j)]=2
                    
                # for all other empty and fresh oranges
                else:
                    vis[(i,j)]=0
                    
                    
                # other than previous if else condition also keep counter of fresh oranges
                if grid[i][j]==1:
                    countFresh+=1
                    
        # print(countFresh, vis)        
        while q:
            [(i,j),t]=q.popleft()
            time=max(time,t)
            # now traverse through all four dirctions by directions array
            # only if its within range, check if its 1 and its visited is equal to 0
            # ie its not converted to 2 already
            # then add it to queue with increased t ie time increase, 
            # and mark it as 2 in visited dictionary

            for d in range(4):
                row,col=i+drow[d],j+dcol[d]
                if row>=0 and row<m and col>=0 and col<n:
               
                    if vis[(row,col)]==0 and grid[row][col]==1:

                        q.append([(row,col),time+1])
                        vis[(row,col)]=2
                        mat[row][col]=2
                        
                        # and reduce fresh oranges count
                        countFresh-=1
                   
        if countFresh>0:
            return -1
        else:
            return time
        
                
        # print(q, mat, vis)

#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends
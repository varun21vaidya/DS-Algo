from collections import deque
class Solution:

    #Function to find distance of nearest 1 in the grid for each cell.
	def nearest(self, grid):
		# Code here
# 		def dfs(i,j,clone,dist,ogi,ogj):
# 		    for d in range(4):
# 		        row,col= drow[d]+i, dcol[d]+j
		        
# 		        if row>=0 and row<m and col>=0 and col<n:
# 		            if clone[row][col]==1:
# 		                dist=min(dist,math.abs(row-ogi)+math.abs(col-ogj))
		               
# 		            dfs(row,col,clone,dist,ogi,ogj)
		          
#             if dist<clone[ogi][ogj]:
#                 clone[ogi][ogj]=dist

        def bfs():
            while q:
                r, c , dist= q.popleft()
                clone[r][c]=dist
                for d in range(4):
                    row,col=drow[d]+r, dcol[d]+c
                    
                    if row>=0 and row<m and col>=0 and col<n:
                        if (row,col) not in vis and grid[row][col]==0:
                            clone[row][col]=dist+1
                            vis.add((row,col))
                            q.append((row,col,dist+1))
            
        m=len(grid)
        n=len(grid[0])
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        clone=[[float('inf')]*n for i in range(m)]
        vis=set()
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    vis.add((i,j))
                    q.append((i,j,0))
                    
        bfs()
    
        return clone
		
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.nearest(grid)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends
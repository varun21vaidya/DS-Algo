from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
		# Code here
		def dfs(i,j, vis, clone, newclr,fillPoint):
		    
		    vis.add((i,j))
		    clone[i][j]=newclr
            
            drow= [-1,0, 1,0]
            dcol= [0,1,0,-1]
            for d in range(4):
                row,col= drow[d]+i, dcol[d]+j

                if row>=0 and row<m and col>=0 and col<n and clone[row][col]==fillPoint and (row,col) not in vis:
                    dfs(row,col,vis,clone,newclr,fillPoint)
                    
                    
        def bfs(i,j,vis,clone,newclr,fillPoint):
            
            vis.add((i,j))
            clone[i][j]=newclr
            
            q= deque()
            q.append((i,j))
            drow= [-1,0, 1,0]
            dcol= [0,1,0,-1]
            
            while q:
                r,c= q.popleft()
                for d in range(4):
                    row,col=drow[d]+r, dcol[d]+c
                    
                    if row>=0 and row<m and col>=0 and col<n and clone[row][col]==fillPoint and (row,col) not in vis:
                        q.append((row,col))
                        vis.add((row,col))
                        clone[row][col]=newclr
            
            
            
        # flood fill should be filled only for all the values of as starting point
        m,n=len(image), len(image[0])
        fillPoint= image[sr][sc]
        clone= image[:]
        vis=set()
        bfs(sr,sc,vis,clone, newColor,fillPoint)
        return clone
        
        
        
        
        
        
#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # we will solve this using bfs as it represents at each step we move distance 1
        
        # 3 things needed clone array for output distance, vis set to track , queue for bfs
        
        # when we find a 0 we will add it to que like that all 0s would be added to q
        # now we will traverse in bfs for each one at a step, so for each step,
        # if there is 1 occured its distance would be added. and we store this distance 
        # in the que itself, to track previous distances and append to it.
        m=len(mat)
        n=len(mat[0])
        clone=[[float('inf')]*n for i in range(m)]
        vis=set()
        q=deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    vis.add((i,j))
                    q.append((i,j,0))
        
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        while q:
            r,c, dist=q.popleft()
            clone[r][c]=dist
                        
            for d in range(4):
                row,col=drow[d]+r, dcol[d]+c
                
                if row>=0 and row<m and col>=0 and col<n:
                    if (row,col) not in vis and mat[row][col]==1:
                        q.append((row,col,dist+1))
                        vis.add((row,col))
                        clone[row][col]=dist+1
        return clone
                        
                    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        m=len(board)
        n=len(board[0])
        vis=set()
        
        def dfs(i,j,vis):
            vis.add((i,j))
            
            for d in range(4):
                row,col=drow[d]+i, dcol[d]+j
                
                if row>=0 and col>=0 and row<m and col<n and (row,col) not in vis and board[row][col]=="O":
                    dfs(row,col,vis)
                    
                    
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j]=="O":
                        dfs(i,j,vis)
                        
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=="O" and (r,c) not in vis:
                    board[r][c]="X"
                    
    
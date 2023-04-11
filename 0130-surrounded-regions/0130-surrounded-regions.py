class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    # now first we need to understand the problem, which states that we need to find
    # the "O"s which are fully surrounded by "X" now it also means we need to skip
    # those "O"s which are on boundry, so from our Jugaad we will find Ulta Solution
    # we will find the "O"s on the boundry store them in visited and then convert those
    # "O"s which are not in visited set.
        
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        m=len(board)
        n=len(board[0])
        vis=set()
        

        # dfs which traverses from boundry and marks those Os which are adjecent to boundry
        # ie these are not eligible to converted
        def dfs(i,j,vis):
            vis.add((i,j))
            
            for d in range(4):
                row,col=drow[d]+i, dcol[d]+j
                
                if row>=0 and col>=0 and row<m and col<n and (row,col) not in vis and board[row][col]=="O":
                    dfs(row,col,vis)
                    
        # traveres throgh matrix but only fetch boundry elements and finds "O"s on boundry and uses dfs on them            
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    if board[i][j]=="O":
                        dfs(i,j,vis)
                        
        # when we got all non eligible marked with vis set, again traverse and convert those Os which are not in vis
        for r in range(m):
            for c in range(n):
                if board[r][c]=="O" and (r,c) not in vis:
                    board[r][c]="X"
                    
    
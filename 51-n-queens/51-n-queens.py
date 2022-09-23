class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        
        def checker(row, col, board, n):
            
            r,c=row,col
            
            # check left side
            while (c>=0):
                if board[r][c]=="Q":
                    return False
                c-=1
                
                
            # check left upward side
            r,c=row,col

            while (r>=0 and c>=0):
                if board[r][c]=="Q":
                    return False
                c-=1
                r-=1
                
            # check left downward side
            r,c=row,col
            while (r<n and c>=0):
                if board[r][c]=="Q":
                    return False
                c-=1
                r+=1
            
            return True
        
        def queens(col,board,n):
            
            if col==n:
                # print(board)
                ans.append(["".join(i) for i in board])
                return
                
            for row in range(n):
                if checker(row,col,board,n):
                    board[row][col]="Q"
                    queens(col+1,board,n)               
                    board[row][col]="."
                
        board=[["." for i in range(n)] for j in range(n)] 
        # print(board)
        ans=[]
        queens(0,board,n)
        return ans
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
#         def isvalid(row,col,board,c):
#             c=str(c)
#             for i in range(9):
#                 if board[i][col]==c: return False
#                 if board[row][i]==c: return False
#                 if board[3*(row//3)+ i//3][3*(col//3) + i%3]==c: return False
                
#             return True
        
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]==".":
#                     for c in range(1,10):
#                         if isvalid(i,j,board,c):
#                             board[i][j]=str(c)                         
#                             if self.solveSudoku(board):
#                                 return True
#                             else:
#                                 board[i][j]="."
#                     return False
#         return True
        
        
        
        # Step by Step Explanation: 
        
        def isvalid(row, col, board, c):
            # c is the number we want to check for this sudodku for that row,col position
            
            for i in range(9):
                
                # check if c already is in same row
                if board[row][i]==c:
                    return False
                
                # check if c already is in same col
                if board[i][col]==c:
                    return False
                
                # check if c already is in same 3*3 box
                # checks for every row and col from this box
                if board[3* (row // 3) + i//3][3* (col//3) + i%3]==c:
                    return False
                
            # if code comes to this level it means there has not been False
            # ie c can be filled in board[row][col]
            return True
        
#       # main function to solve sudoku
        # traverse through matrix 
        for i in range(9):
            for j in range(9):

                # check if there is any empty cell
                if board[i][j]==".":

                    # if there is any empty cell we will check for all values from 1 to 9
                    for c in range(1,10):
                        c=str(c)

                        # now call isvalid to check if c can be filled in board at i,j position
                        if isvalid(i,j,board,c):

                            # if isvalid is true then fill the c in the position
                            # then we can use recursion to check if it can fulfill 
                            # for other empty cells or not if it fulfill we will not remove its value 
                            # and will return true
                            # but if sudoku at any point in future for a certain position could not match 
                            # any value for that empty position then that will return False
                            # and through backtracking we will come to this point which was wrong fill for this sudoku
                            # so as it was wrong fill for this position then we will remove c from the board

                            board[i][j]=c

                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j]="."

                        # even after checking for loop with isvalid from 1->9 for this position
                        # if none of the value gets filled that means at some previous point it was wrong fill 
                        # so backtracking to that previous wrong fill point
                        # it will return false which will return sodoku(board) to false and will empty that cell again
                    # and check for next valid value for that position
                    return False

        # if it comes here, it means there is no empty cell remaining 
        return True

    
    
    
    
    
    
    
    
    
# # Same code without comments

    
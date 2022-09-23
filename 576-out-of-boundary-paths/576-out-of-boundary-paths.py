class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @lru_cache(None)
        def helper(move,row,col):
            if (row==m or row<0 or col<0 or col==n):
                return 1
            if move==0: return 0
            move-=1
            
            return ((helper(move, row+1, col)+
                    helper(move, row-1, col)+
                   helper(move, row, col+1)+
                   helper(move, row, col-1))%(1000000000+7))
        
        return helper(maxMove, startRow, startColumn)
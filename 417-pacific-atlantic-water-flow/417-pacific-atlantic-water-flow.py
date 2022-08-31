class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows , cols = len(heights), len(heights[0])
        pacific , atlantic  = set(), set()
        
        # dfs solution
        def check(r, c ,visited, prevHeight):
            if((r,c) in visited or r<0 or c<0 or r==rows or c==cols or
              heights[r][c]<prevHeight):
                return 
            visited.add((r,c))
            # checking for 4 adjacent cells 
            check(r+1,c,visited,heights[r][c])
            check(r-1,c,visited,heights[r][c])
            check(r, c+1, visited, heights[r][c])
            check(r, c-1, visited, heights[r][c])
            
        
        # top and bottom row - pacific and atlantic ocean resp
        for c in range(cols):
            check(0, c ,pacific,heights[0][c])
            check(rows-1,c,atlantic, heights[rows-1][c])
            
        # first and last col - pacific and atlantic ocean resp   
        for r in range(rows):
            check(r,0,pacific,heights[r][0])
            check(r,cols-1,atlantic,heights[r][cols-1])
            
        return pacific & atlantic 
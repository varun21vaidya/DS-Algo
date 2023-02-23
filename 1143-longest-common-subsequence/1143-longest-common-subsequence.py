class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         # recursive
#         def solver(x,y,text1, text2):
#             if  x==0 or y==0:
#                 return 0
            
#             if text1[x-1]==text2[y-1]:
#                 return 1+ solver(x-1, y-1,text1,text2)
            
#             return max( solver(x, y-1,text1,text2), solver(x-1, y,text1,text2))
    
#         return solver(len(text1),len(text2), text1,text2) 
    
        # Memoization:
        
        def solver(x,y):
            if x==0 or y==0:
                return 0
            
            if dp[x][y]!=-1:
                return dp[x][y]
            
            if text1[x-1]==text2[y-1]:
                dp[x][y]= 1 + solver(x-1,y-1)
            else:
                dp[x][y]= max(solver(x,y-1),solver(x-1,y))
            
            return dp[x][y]
        
        dp=[[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        solver(len(text1),len(text2))
        # print(dp) 
        return dp[-1][-1]
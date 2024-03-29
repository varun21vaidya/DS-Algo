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
        
#         def solver(x,y):
#             if x==0 or y==0:
#                 return 0
            
#             if dp[x][y]!=-1:
#                 return dp[x][y]
            
#             if text1[x-1]==text2[y-1]:
#                 dp[x][y]= 1 + solver(x-1,y-1)
#             else:
#                 dp[x][y]= max(solver(x,y-1),solver(x-1,y))
            
#             return dp[x][y]
        
#         dp=[[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         return solver(len(text1),len(text2))


        # Tabulation:
        dp=[[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        x,y=len(text1),len(text2)
        for i in range(x+1):
            for j in range(y+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif text1[i-1]==text2[j-1]:
                    dp[i][j]=1+ dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[x][y]
            
        
        
        
# # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        # # For printing LCS: 
        
#         # recursive
#         def solver(x,y,temp):
#             if  x==0 or y==0:
#                 return ""
            
#             if text1[x-1]==text2[y-1]:
#                 temp=text1[x-1]+ solver(x-1, y-1,temp)
#                 return temp
            
#             a=solver(x, y-1,temp)
#             b=solver(x-1, y,temp)
#             temp= max(a,b,key=len)
#             return temp
            
#         temp=""
#         res=solver(len(text1),len(text2),temp) 
#         return (res)
    
        # Memoization:
        
#         def solver(x,y):
#             if x==0 or y==0:
#                 return ""
            
#             if dp[x][y]!="":
#                 return dp[x][y]
            
#             if text1[x-1]==text2[y-1]:
#                 dp[x][y]= text1[x-1]+solver(x-1,y-1)
#             else:
#                 dp[x][y]= max(solver(x,y-1),solver(x-1,y),key=len)
                
#             return dp[x][y]
        
#         dp=[["" for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         res=solver(len(text1),len(text2))

#         return((res))


#         # Tabulation:
#         dp=[["" for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         x,y=len(text1),len(text2)
#         for i in range(x+1):
#             for j in range(y+1):
#                 if i==0 or j==0:
#                     dp[i][j]=""
#                 elif text1[i-1]==text2[j-1]:
#                     dp[i][j]=text1[i-1]+ dp[i-1][j-1]
#                 else:
#                     dp[i][j]=max(dp[i-1][j],dp[i][j-1],key=len)
#         res=dp[x][y]
        
#         return (res)
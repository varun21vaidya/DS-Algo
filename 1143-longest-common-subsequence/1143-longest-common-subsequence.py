class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
#         # recursive
#         def solver(x,y,temp,res):
#             if  x==0 or y==0:
#                 return ""
            
#             if text1[x-1]==text2[y-1]:
#                 temp=+text1[x-1]+ solver(x-1, y-1,temp,res)
#                 if len(temp)>len(res[0]): res[0]=temp
#                 return temp
            
#             a=solver(x, y-1,temp,res)
#             b=solver(x-1, y,temp,res)
#             if len(a)>len(b):
#                 temp=a
#             else:
#                 temp=b
#             if len(temp)>len(res[0]): res[0]=temp
#             return temp
            
#         temp=""
#         res=[""]
#         solver(len(text1),len(text2),temp,res) 
#         print(res)
#         return len(res[0])
    
        # Memoization:
        
        def solver(x,y):
            if x==0 or y==0:
                return ""
            
            if dp[x][y]!="":
                return dp[x][y]
            
            if text1[x-1]==text2[y-1]:
                dp[x][y]= text1[x-1]+solver(x-1,y-1)
            else:
                dp[x][y]= max(solver(x,y-1),solver(x-1,y),key=len)
                
            return dp[x][y]
        
        dp=[["" for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        x=solver(len(text1),len(text2))
        print(x)
        return(len(x))


        # Tabulation:
#         dp=[[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
#         x,y=len(text1),len(text2)
#         for i in range(x+1):
#             for j in range(y+1):
#                 if i==0 or j==0:
#                     dp[i][j]=0
#                 elif text1[i-1]==text2[j-1]:
#                     dp[i][j]=1+ dp[i-1][j-1]
#                 else:
#                     dp[i][j]=max(dp[i-1][j],dp[i][j-1])
#         return dp[x][y]
                
        
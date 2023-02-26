class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
#         def solver(word1,i,word2, j):
#             if i==0:
#                 return j
#             elif j==0:
#                 return i
            
#             elif word1[i-1]==word2[j-1]:
#                 return solver(word1,i-1,word2,j-1)
            
#             insert=solver(word1,i,word2, j-1)
#             replace=solver(word1,i-1,word2, j-1)
#             delete=solver(word1,i-1,word2, j)
            
#             return min(insert, replace, delete)+1

#         return solver(word1,len(word1),word2, len(word2))

        def solver(word1,i,word2, j):
            if i==0:
                dp[i][j]= j
            elif j==0:
                dp[i][j]= i
            
            elif dp[i][j]!=-1:
                return dp[i][j]
            
            elif word1[i-1]==word2[j-1]:
                dp[i][j]= solver(word1,i-1,word2,j-1)
            
            else:
                insert=solver(word1,i,word2, j-1)
                replace=solver(word1,i-1,word2, j-1)
                delete=solver(word1,i-1,word2, j)

                dp[i][j]= min(insert, replace, delete)+1
            
            return dp[i][j]

        dp=[[-1 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        return solver(word1,len(word1),word2, len(word2))
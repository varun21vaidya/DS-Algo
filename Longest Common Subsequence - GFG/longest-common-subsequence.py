#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # def solver(x,y):
        #     if x==0 or y==0:
        #         return 0
            
        #     if s1[x-1] == s2[y-1]:
        #         return 1+ solver(x-1,y-1)
            
        #     return max(solver(x,y-1), solver(x-1,y))
        
        # return solver(x,y)
        
        # # # -------------------------------------
        
        # def solver(x,y):
        #     if x==0 or y==0:
        #         return 0
        
        #     if dp[x][y]!=-1:
        #         return dp[x][y]
                
        #     if s1[x-1] == s2[y-1]:
        #         dp[x][y]= 1+ solver(x-1,y-1)
                
        #     else:
        #         dp[x][y]= max(solver(x,y-1), solver(x-1,y))
                
        #     return dp[x][y]
        
        # dp=[[-1 for _ in range(y+1)] for _ in range(x+1)]
        # return solver(x,y)

        # # --------------------------------------
        
        dp=[[0 for _ in range(y+1)] for _ in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j],dp[i][j-1])
            
        return dp[x][y]
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
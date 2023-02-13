#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
    #   RECURSIVE APPROACH: 
        # def solver(W, wt, val, n):
        #     if n==0 or W==0:
        #         return 0
            
        #     if wt[n-1]<=W:
        #         return max(val[n-1]+ solver(W-wt[n-1], wt, val, n-1),
        #         solver(W, wt, val, n-1))
                
        #     else:
        #         return solver(W, wt, val, n-1)
                
        # return solver(W, wt, val, n)
    
    # DYNAMIC PROGRAMMING - MEMOIZATION
        # def solver(W, n):
        #     if n==0 or W==0:
        #         return 0
                
        #     if dp[n][W]!=-1:
        #         return dp[n][W]
                
        #     if wt[n-1]<=W:
        #         dp[n][W]=max(val[n-1]+ solver(W-wt[n-1], n-1),
        #         solver(W, n-1))
                
        #     else:
        #         dp[n][W]= solver(W, n-1)
        
        #     return dp[n][W]
         
        # dp=[[-1 for _ in range(W+1)] for _ in range(n+1)]       
        # # print(dp)
        # return solver(W,n)
        
        # DP - BOTTOM UP APPRAOCH
        dp=[[0]*(W+1) for _ in range(n+1)]  
        for row in range(1,n+1):
            for col in range(1,W+1):
                # replace n,W with row and col
                if wt[row-1]<=col:
                    dp[row][col]= max(val[row-1]+ dp[row-1][col-wt[row-1]], dp[row-1][col])
                
                else:
                    dp[row][col]=dp[row-1][col]
                
        return dp[-1][-1]
        


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
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
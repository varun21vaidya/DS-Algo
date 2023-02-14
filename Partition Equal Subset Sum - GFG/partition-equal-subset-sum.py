# User function Template for Python3

class Solution:
    def equalPartition(self, N, arr):
        # code here
        w=sum(arr)
        if w%2==1:
            return False
        w=w//2
        dp= [[0 for _ in range(w+1)] for _ in range(N+1)]
        for firstcol in range(N+1):
            dp[firstcol][0]=1
        
        for row in range(1,N+1):
            for col in range(1,w+1):
                if arr[row-1]<=col:
                    dp[row][col]=max(dp[row-1][col- arr[row-1]], dp[row-1][col])
                else:
                    dp[row][col]=dp[row-1][col]
        return dp[N][w]

#{ 
 # Driver Code Starts
# Initial Template for Python3

import sys
input = sys.stdin.readline
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for it in range(N):
            arr[it] = int(arr[it])
        
        ob = Solution()
        if (ob.equalPartition(N, arr) == 1):
            print("YES")
        else:
            print("NO")
# } Driver Code Ends
#User function Template for python3
class Solution:
	def minDifference(self, arr, n):
		# code here
        # def solver(n,w,diff):
        #     if n==0:
        #         x=abs(w-(W-w))
        #         if diff>x:
        #             diff=x
        #         return diff
            
        #     if arr[n-1]<=w:
        #         diff= min(solver(n-1,w-arr[n-1],diff), solver(n-1,w,diff))
        #     else:
        #         diff= solver(n-1,w,diff)
            
        #     return diff
        
        # W=sum(arr)
        # w=W
        
        # return solver(n,w,float('inf'))
    
    
        # # Memoization
        
        # def solver(n,w,dp):
        #     if n==0:
        #         x=abs(w-(W-w))
        #         if dp[n][w]>x:
        #             dp[n][w]=x
        #         return dp[n][w]
            
        #     if w==0:
        #         dp[n][w]=0
        #         return dp[n][w]
                
        #     if dp[n][w]!=float('inf'):
        #         return dp[n][w]
            
        #     if arr[n-1]<=w:
        #         dp[n][w]= min(solver(n-1,w-arr[n-1],dp), solver(n-1,w,dp))
        #     else:
        #         dp[n][w]= solver(n-1,w,dp)
            
        #     return dp[n][w]
        
        # W=sum(arr)
        # w=W
        # dp=[[float('inf') for _ in range(w+1)]for _ in range(n+1)]
        # return solver(n,w,dp)
        
        
        # # # Bottom Up Appraoch:
        W=sum(arr)
        w=W
        dp=[[float('inf') for _ in range(w+1)]for _ in range(n+1)]
        for i in range(n+1):
            for j in range(w+1):
                if i==0:
                    x=abs(j-(W-j))
                    if dp[i][j]>x:
                        dp[i][j]=x
                # if j==0:
                #     dp[i][j]=0
                        
                elif arr[i-1]<=j:
                    dp[i][j]= min(dp[i-1][j-arr[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[n][w]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minDifference(arr, N)
		print(ans)

# } Driver Code Ends
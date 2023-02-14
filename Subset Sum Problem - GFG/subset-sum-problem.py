#User function Template for python3

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        # def solver(n,w):
        #     if n==0 or w<0: return False
        #     if w==0: return True
        #     if arr[n-1]<=w:
        #         return solver(n-1, w-arr[n-1]) or solver(n-1,w)
        #     else:
        #         return solver(n-1, w)
            
        #     return False
        
        # return solver(N,sum)
        
        # def solver(n,w):
        #     if n==0 or w<0:
        #         return False
        #     if w==0:
        #         dp[n][w]=1
        #         return True
                
        #     if dp[n][w]!=0:
        #         return dp[n][w]
                
        #     if arr[n-1]<=w:
        #         dp[n][w]=solver(n-1, w-arr[n-1]) or solver(n-1,w)
        #     else:
        #         dp[n][w]= solver(n-1, w)
                
        #     return dp[n][w]
        
        # dp=[[0 for _ in range(sum+1)] for _ in range(N+1)]
        # return solver(N,sum)


        dp=[[0 for _ in range(sum+1)] for _ in range(N+1)]
        # for weight =0 there always be True
        for firstcol in range(N+1):
            dp[firstcol][0]=1
            
        for row in range(1,N+1):
            for col in range(1,sum+1):
                if arr[row-1]<=col:
                    dp[row][col]=dp[row-1][col-arr[row-1]] or dp[row-1][col]
                else:
                    dp[row][col]= dp[row-1][col]
        
        return dp[N][sum]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
#User function Template for python3

class Solution:
    def cutRod(self, price, N):
        #code here
        
        # # this is literally same code as unbounded knapsack
        # # just observe that like knapsack value array here is price array, and N as constant ie weight
        # # and we are asked max prifit 
        # # now we need a array which will be compared with N, ie we need rod lengths
        # # from which we will take prices, so create a length array 
        
        # # Recurison + Memoization
        # def solver(n,w):
        #     if n==0 or w==0:
        #         return 0
        #     if dp[n][w]:
        #         return dp[n][w]
        #     if length[n-1]<=w:
        #         dp[n][w]= max(price[n-1]+solver(n,w-length[n-1]), solver(n-1,w))
        #     else:
        #         dp[n][w]= solver(n-1,w)
            
        #     return dp[n][w]
        
        # length=[i for i in range(1, N+1)]
        # dp=[[0 for _ in range(N+1)] for _  in range(N+1)]
        # return solver(N,N)


        # # Bottom UP Approach:
        
        # length=[i for i in range(1,N+1)] --> 1 2 3 4 5 6 7 8
        # but we can directly eliminate by taking i directly instead of length[i-1]
        # as we are anyway iterating i loop for that so no need for 2nd array
        
        dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
        for i in range(N+1):
            for j in range(N+1):
                if i==0 or j==0:
                    dp[i][j]=0
                elif i<=j:
                    dp[i][j]=max(price[i-1]+dp[i][j - i],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
                    
        return dp[N][N]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
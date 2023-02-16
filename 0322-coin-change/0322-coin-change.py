class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    

        # # # RECURSIVE SOLUTION:

        # def solver(n,w,count):
        #     # if sum is 0 and we have some coins, we dont need any of them
        #     # and if w==0 and n==0 then also we dont have coins and dont need them
        #     if w==0:
        #         return 0

        #     # *****if we need amount 5 and we have empty jar, how can we give them any amount
        #     # we would need infinite coins to get 5 amount from empty ie impossible
        #     # therefor for empty jar ie n==0 return infinity

        #     if n==0:
        #         return float('inf')
            
        #     if coins[n-1]<=w:
        #         count= min(1+solver(n,w-coins[n-1],count),solver(n-1,w,count))
        #     else:
        #         count= solver(n-1,w,count)
            
        #     return count

        # x=solver(len(coins), amount,0)
        # if x==float('inf'):
        #     return -1
        # else:
        #     return x


        # # # Memoization

        # def solver(n,w,dp):
        #     # if sum is 0 and we have some coins, we dont need any of them
        #     # and if w==0 and n==0 then also we dont have coins and dont need them
        #     if w==0:
        #         return 0

        #     # *****if we need amount 5 and we have empty jar, how can we give them any amount
        #     # we would need infinite coins to get 5 amount from empty ie impossible
        #     # therefor for empty jar ie n==0 return infinity
        #     if n==0:
        #         return float('inf')

        #     if dp[n][w]!=amount+1:
        #         return dp[n][w]
            
        #     elif coins[n-1]<=w:
        #         dp[n][w]=min(1+ solver(n,w-coins[n-1],dp), solver(n-1,w,dp))
        #     else:
        #         dp[n][w]=solver(n-1,w,dp)

        #     return dp[n][w]

        # n=len(coins)
        # # # we can use amount +1 for initialization as indicator to max value which 
        # # # does not interfere with float('inf') of n==0
        # dp=[[amount+1 for _ in range(amount+1)] for _ in range(n+1)]
        # x=solver(n,amount,dp)
        # if x!=float('inf'):
        #     return x
        # else:
        #     return -1



        # # Bottom Up Approach:

        # n=len(coins)
        # dp=[[float('inf') for _ in range(amount+1)] for _ in range(n+1)]

        # if amount==0: return 0  
        # for i in range(n+1):
        #     for j in range(amount+1):
        #         if i==0:
        #             dp[i][j]=float('inf')
        #         if j==0:
        #             dp[i][j]=0
        #         elif coins[i-1]<=j:
        #             dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        #         else:
        #             dp[i][j]= dp[i-1][j]
        # if dp[n][amount]!=float('inf'):
        #     return dp[n][amount]
        # else:
        #     return -1


        # # Space Optimized to 1D array
        # # we can also use 
        dp=[float('inf')]* (amount+1)
        dp[0]=0
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if coins[i-1]<=j:
                    dp[j]=min(dp[j] ,1+dp[j-coins[i-1]])
        
        return dp[amount] if dp[amount]!=float('inf') else -1
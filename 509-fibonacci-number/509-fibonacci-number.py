class Solution:
    def fib(self, n: int) -> int:
        # if n<=1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        
        # a,b=0,1
        # if n<=1:
        #     return n
        # for _ in range(n-1):
        #     a,b=b,a+b
        # return b
    
        dp=[0,1]
        for i in range(2,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]
            
                
                
                
    
    
class Solution:
    def numTrees(self, n: int) -> int:
        def catlon(n):
            if n<=1:
                return 1
            res=0
            if n in dp:
                return dp[n]
            for i in range(n):
                dp[i]=catlon(i)
                dp[n-i-1]=catlon(n-i-1)
                res+=dp[i]*dp[n-i-1]
            
            return res
        
        dp={}
        return catlon(n)
class Solution:
    def numTrees(self, n: int) -> int:

    # # BEHIND THE INTUTION
    
    # We know that all node in left subtree are smaller than root and in right subtree are larger than root
    # so if we have ith number as root, all numbers from 1 to i-1 will be in left subtree and
    # i+1 to N will be in right subtree. 
    # If 1 to i-1 can form x different trees and i+1 to N can from y different trees 
    # then we will have x*y total trees when ith number is root and we also have N choices for root
    # also so we can simply iterate from 1 to N for root and another loop for left and right subtree.
    # If we take a closer look, we can notice that the count is basically n’th Catalan number.
    
    # Catalan numbers are defined as a mathematical sequence that consists of positive integers,
    # which can be used to find the number of possibilities of various combinations. 
    
    # Approach: 
    
    # Base condition for the recursive approach, when n <= 1, return 1
    # Iterate from i = 0 to i < n
    # Make a recursive call catalan(i) and catalan(n – i – 1) and keep adding the product of both into res.
    # Return the res.
    
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
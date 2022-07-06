class Solution:
    def fib(self, n: int) -> int:
        # if n<=1:
        #     return n
        # return self.fib(n-1)+self.fib(n-2)
        a,b=0,1
        if n<=1:
            return n
        for _ in range(n-1):
            a,b=b,a+b
        return b
            
                
                
                
    
    
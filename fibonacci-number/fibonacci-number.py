class Solution:
    def fib(self, n: int) -> int:
        # if n<2:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib (n-2)
        
        def solver(n,mapp):
            if n<2:
                mapp[n]=mapp.get(n,n)
            else:
                mapp[n]=mapp.get(n,solver(n-1,mapp)+solver(n-2,mapp))
            return mapp[n]
        
        mapp={}
        return solver(n,mapp)
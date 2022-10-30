class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        # print(digits)
        # Brute Force (TLE)
        # res=0
        # def summ(x):
        #     s=0
        #     while x:
        #         s,x=s+x%10,x//10
        #     return s
        # while True:
        #     x=n+res
        #     if summ(x)<=target:
        #         break
        #     res+=1
        # return res
        
        
        res=0
        m=1
        def summ(x):
            s=0
            while x:
                s,x=s+x%10,x//10
            return s
        while summ(n+res)>target:
            m*=10
            res=m-n%m
        return res
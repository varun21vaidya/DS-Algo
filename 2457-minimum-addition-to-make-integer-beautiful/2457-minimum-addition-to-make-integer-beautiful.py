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
        p=1
        def summ(x):
            s=0
            while x:
                s,x=s+x%10,x//10
            return s
        while summ(n)>target:
            res+=(10-n%10)*p    
            n//=10
            n+=1
            p*=10
        return res
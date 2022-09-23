class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n==3^x
        # take log on both sides which will give log n == x log 3
        # so x = log n/ log 3
        # if x is integer return true
        
        def log3(x):
            return math.log10(x)/math.log10(3)
        if n<=0: return False
        return math.ceil(log3(n))==math.floor(log3(n))
            
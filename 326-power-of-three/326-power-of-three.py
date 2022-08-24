class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def log3(x):
            return math.log10(x)/math.log10(3)
        if n<=0: return False
        return math.ceil(log3(n))==math.floor(log3(n))
            
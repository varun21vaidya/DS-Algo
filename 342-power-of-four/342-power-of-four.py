class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        # we  take the log of the number on base 4 and 
        # if we get an integer then the number is the power of 4
        
        if n<=0:
            return False
        def log4(z):
            return (math.log10(z)/math.log10(4))
                    
        return math.ceil(log4(n))==math.floor(log4(n))
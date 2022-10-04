class Solution:
    def climbStairs(self, n: int) -> int:
    
    # recursive, TLE
#         def steps(n):
#             if n<3: return n
            
#             return steps(n-1)+steps(n-2)
        
#         return steps(n)
        
    # dictionary
        mapp={}
        def steps(n):
            if n<3: return n
            if n in mapp: return mapp[n]
            
            mapp[n]=steps(n-1)+steps(n-2)
            return mapp[n]
        return steps(n)
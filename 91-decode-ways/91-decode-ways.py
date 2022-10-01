class Solution:
    def numDecodings(self, s: str) -> int:
        
        
#         # as we can see 11106 can be divided into two valid values
#         # 1,1,10,6 and  11,10,6 
#         # so what we have to do is split the values either with fist digit
#         # or first two digits considering they are valid
#         # but how, its simple that values greater than 10 
#         # can only be with two digits and the limit will be 26
#         # SO we will use recursion to get values from both methods
#         # by only with first digit which have to be under 1<= to >=9
#         # and firsttwo digits which will take first two digits and
#         # remaining string will again be evaluated on these two conditions
#         # and final result will be combination of both of them
        
#         def solver(s):
#             if not  s: return 1
            
#             first, firsttwo = 0,0
            
#             if 1<=int(s[:1])<=9:
#                 first= solver(s[1:])
                
#             if 10<=int(s[:2])<=26:
#                 firsttwo= solver(s[2:])
                
#             return first + firsttwo
        
        
        # now we can see if the input is 1111111111111...it will give TLE
        # because we are iterating already known input so 
        # if we can eliminate these repitations we can get an efficient solution
        # so to improve we can use memoization in this recursive solution       
        # so this will be dp solution with memoization approach
        
        def solver(s,dp):
            if not  s: return 1
            
            first, firsttwo = 0,0
            
            if s in dp:
                return dp[s]
            
            if 1<=int(s[:1])<=9:
                first= solver(s[1:],dp)
                
            if 10<=int(s[:2])<=26:
                firsttwo= solver(s[2:],dp)
                
            dp[s]= first + firsttwo
            
            return dp[s]
        
        
        dp={}       
        return solver(s,dp)
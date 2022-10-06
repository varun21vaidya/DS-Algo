class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        # TLE
        
        # if observed carefully, the result number is combination of 
        # its previous number and its compliment
        # for 3 its "01" + "10" and "01" was 2
        # for 4 its "0110" + "1001" and "0110" was 3 like that
        # so we can recursively call the previous number 
        # and create its compliment or inverse and return the combination
        
#         def solved(n):
#             if n==1: return "0"
            
#             s=solved(n-1)
#             new=""
#             for i in s:
#                 new+=mapp[i]
#             return s+new
            

#         mapp={'0':'1','1':'0'}
#         return solved(n)[k-1]
    
        # similar approach just changed inverse method
        # memory exceeded
#         def solved(n):
#             if n==1: return "0"
            
#             s=solved(n-1)
#             new=bin(int(s,2)^(2**(len(s)+1)-1))[3:]
#             return s+new
            
#         return solved(n)[k-1]


        if n==1:
            return 0
        
        mid=2**(n-2)
        
        if k<=mid:
            return self.kthGrammar(n-1,k)
        else:
            if self.kthGrammar(n-1,k-mid)==1:
                return 0
            else:
                return 1

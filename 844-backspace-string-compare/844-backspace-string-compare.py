#https://leetcode.com/problems/backspace-string-compare/
#(Asked in Amazon SDE1 interview)

# Runtime: 43 ms, faster than 55.97% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 98.49% of Python3 online submissions for Backspace String Compare.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def realstr(s):
            real=[]
            for i in s:
                if i!="#":
                    real.append(i)
                else:
                    if real:
                        real.pop()   
            return real
        
        return realstr(s)==realstr(t)
    

#BETTER SOLUTION    
    
#Runtime: 20 ms, faster than 99.27% of Python3 online submissions for Backspace String Compare.
#Memory Usage: 14.1 MB, less than 93.90% of Python3 online submissions for Backspace String Compare.

# class Solution:
#     def soln(self, lst: str)-> list:
#         op=[]
#         for i in lst:
#             if i=="#" and op:
#                op.pop()
#             elif i!="#":
#                 op.append(i)        
#         return op
    
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         return self.soln(s)==self.soln(t)

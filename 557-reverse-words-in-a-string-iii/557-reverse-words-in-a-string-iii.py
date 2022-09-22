class Solution:
    def reverseWords(self, s: str) -> str:
        
        ans=""
        s=s.split()
        for i in s:
            ans+=i[::-1]+" "
        return ans[:-1]
    
#         ans=""
#         temp=""
#         for i in s:
#             if i==" ":
#                 ans+=temp+" "
#                 temp=""
#             else:
#                 temp=i+temp
                
#         return ans+temp
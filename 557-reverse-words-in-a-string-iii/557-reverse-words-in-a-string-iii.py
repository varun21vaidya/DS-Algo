class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        temp=""
        for i in s:
            if i==" ":
                ans+=temp+" "
                temp=""
            else:
                temp=i+temp
                
        return ans+temp
class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.strip().split()
        return " ".join(s[::-1])
        
        # return " ".join(s.split()[::-1])
    
        # lst=s.split(" ")
        # temp=""
        # for i in lst[::-1]:
        #     if i!="":
        #         temp+=i+" "
        # return temp[:-1]
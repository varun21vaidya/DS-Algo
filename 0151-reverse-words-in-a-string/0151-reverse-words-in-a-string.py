class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
        # lst=s.split(" ")
        # temp=""
        # for i in lst[::-1]:
        #     if i!="":
        #         temp+=i+" "
        # return temp[:-1]
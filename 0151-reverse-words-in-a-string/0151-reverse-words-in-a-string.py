class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split(" ")
        temp=""
        for i in lst[::-1]:
            if i!="":
                temp+=i+" "
        return temp[:-1]
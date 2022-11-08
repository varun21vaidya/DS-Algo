class Solution:
    def makeGood(self, s: str) -> str:
        def check(s):
            return ord(s[i])+32==ord(s[i+1]) or ord(s[i])==ord(s[i+1])+32
        for _ in range(len(s)//2):
            for i in range(len(s)-1):
                if check(s):
                    s=s.replace(s[i:i+2],"")
                    break
        return (s)

    
class Solution:
    def makeGood(self, s: str) -> str:
        # Brute Force
        
        # def check(s):
        #     return ord(s[i])+32==ord(s[i+1]) or ord(s[i])==ord(s[i+1])+32
        # for _ in range(len(s)//2):
        #     for i in range(len(s)-1):
        #         if check(s):
        #             s=s.replace(s[i:i+2],"")
        #             break
        # return (s)

        stack=[]
        for i in s:
            if stack:
                if abs(ord(stack[-1])-ord(i))==32:
                    stack.pop()
                else:
                    stack.append(i)
                
            else:
                stack.append(i)
        return "".join(stack)
    
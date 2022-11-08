class Solution:
    def makeGood(self, s: str) -> str:
        # temp=""
        # i=0
        # def check(s):
        #     return ord(s[i])+32==ord(s[i+1]) or ord(s[i])==ord(s[i+1])+32
        # while i<len(s)-1:
        #     if :
        #         i+=2
        #     else:
        #         temp+=s[i]
        #         i+=1
        # return (temp)

        # If we find a pair in 's', remove this pair from 's'
        # and solve the remaining string recursively.
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood(s[:i] + s[i + 2:])
        
        # Base case, if we can't find a pair, just return 's'.
        return s
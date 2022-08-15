class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot = 0
        curr = 0
        pre = 0
        for i in range(len(s)):
            curr = d[s[i]]
            if curr>pre :
                tot = tot+ curr- (2*pre)
            else:
                tot = tot + curr
            pre = curr
        return tot
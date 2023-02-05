class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        countp=Counter(p)
        res=[]
        for i in range(len(s)-len(p)+1):
            new=Counter(s[i:i+len(p)])
            if new==countp:
                res.append(i)
        return res
            
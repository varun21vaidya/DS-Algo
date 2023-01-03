class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        sor=[]
        ans=0
        for i in range(m):
            s=""
            for j in range(n):
                s+=strs[j][i]
            if s!="".join(sorted(s)):
                ans+=1
        return ans
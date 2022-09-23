class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapp=dict()
        for i in s:
            mapp[i]=mapp.get(i,0)+1
        # print(mapp)
        for i in mapp:
            if mapp[i]==1:
                return list(s).index(i)
        return -1
        
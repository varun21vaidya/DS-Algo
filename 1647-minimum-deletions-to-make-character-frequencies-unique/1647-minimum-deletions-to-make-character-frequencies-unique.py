class Solution:
    def minDeletions(self, s: str) -> int:
        mapp={}
        for i in s:
            mapp[i]=mapp.get(i,0)+1
        # print(mapp)
        freq=list(mapp.values())
        # print(freq)
        cnt=0
        for i in range(len(freq)):
            if freq[i] in freq[:i]+freq[i+1:]:
                while freq[i]-1 in freq and freq[i]>=0:
                    freq[i]-=1
                    cnt+=1
                    if freq[i]<=0:
                        break
                if freq[i]>0:
                    freq[i]-=1
                    cnt+=1
        return cnt
            
        
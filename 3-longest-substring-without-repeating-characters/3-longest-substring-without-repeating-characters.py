class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,maxx=0,0,0
        if not s: return 0
        mapp=dict()
        while j<len(s):
            mapp[s[j]]=mapp.get(s[j],0)+1
            
            if (len(mapp)==(j-i+1)):
                maxx=max(maxx,(j-i+1))
                j+=1
        
            elif (len(mapp)<(j-i+1)):
                while (len(mapp)<(j-i+1)):
                    mapp[s[i]]-=1
                    if mapp[s[i]]==0:
                        del mapp[s[i]]
                    i+=1
                j+=1
        
        if maxx: return maxx
        else: return -1
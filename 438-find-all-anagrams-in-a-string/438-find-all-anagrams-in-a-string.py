class Solution:
    def findAnagrams(self, txt: str, pat: str) -> List[int]:
        
#         HAHA GOT TLE FOR THIS O(n2)
        # ls,lp,sortp=len(s),len(p),sorted(p)
        # return [i for i in range(ls-lp+1) if sorted(s[i:i+lp])==sortp]
        
        
        #Approach Sliding Window
	    #Initialization part
        i,j,res=0,0,[]
        mapp,patmap=dict(),dict()
        for p in pat:
            patmap[p]=patmap.get(p,0)+1
	   # print(patmap)
	   
	   #loop part
        while j<len(txt):

            #calculation part
            mapp[txt[j]]=mapp.get(txt[j],0)+1

            #condition part
            if (j-i+1)==len(pat):

                # print(mapp)

                #ANS part
                if mapp==patmap:
                    res.append(i)
                mapp[txt[i]]-=1
                if mapp[txt[i]]==0: mapp.pop(txt[i])
                i+=1
            j+=1

        return res
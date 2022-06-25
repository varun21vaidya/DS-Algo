class Solution:
    def findAnagrams(self, txt: str, pat: str) -> List[int]:
        
#         HAHA GOT TLE FOR THIS O(n2)
        # ls,lp,sortp=len(s),len(p),sorted(p)
        # return [i for i in range(ls-lp+1) if sorted(s[i:i+lp])==sortp]
        
        
        
        
       # So one way was to calculate all anagrams of pat
	   # and find those in txt
	   # but calculting only anagram would be O(n!)
	    
	    
	   # Approach: Sliding Window
	   # As there is string, substring and fixed window(len of substring)
	   # we can use sliding window for this
	    
	   # so parts of sliding window:
	   # initialization, while loop, calculation part, condition and ans part
	    
	   # so here for each sliding window we can check which letters are present
	   # and are the number of each letters(count) same for window and pat
	   # if yes to both then its anagram of pat
	    
	   # so if we are considering count of strings we will use dictionary
	    
	   # so first we will create counted dictionary of pat
	   # now come to calulation part, for each sliding window we will 
	   # either update count by 1 or if its not there create count with default 0 +1
	    
	   # and in the ans part, if both dicitonaries are same append index of i ie start to res
	   # and with each slide drop arr[i] from dictionary value and if its 0 remove it
        
        
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
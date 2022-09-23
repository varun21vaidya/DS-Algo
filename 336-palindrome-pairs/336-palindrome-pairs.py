class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans =set()
        val_pos = {w:idx for idx,w in enumerate(words)}
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                pref = word[:j] 
                suf = word[j:]
                inv_pref = pref[::-1]
                inv_suf = suf[::-1]
                if(pref==inv_pref):
                    if(inv_suf in val_pos and val_pos[inv_suf]!=i):ans.add((val_pos[inv_suf],i))
            
                if(suf==inv_suf):
                    if(inv_pref in val_pos and val_pos[inv_pref]!=i):ans.add((i,val_pos[inv_pref]))

        return [list(pair) for pair in ans]
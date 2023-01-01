class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string=list(s.split())
        if len(pattern)!=len(string):
            return False
        mapp={}
        for i in range(len(string)):
            if pattern[i] in mapp:
                if mapp[pattern[i]]!=string[i]:
                    return False
            mapp[pattern[i]]=string[i]
        
        if len(mapp.values())!=len(set(mapp.values())):
            return False
            
        return True
                

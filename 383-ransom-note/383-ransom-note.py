class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if len(magazine)<len(ransomNote):
        #     return False
        # m= Counter(magazine)
        # # print(m)
        # count=0
        # for r in ransomNote:
        #     if m[r]>0:
        #         m[r]-=1
        #         count+=1
        # # print(m, count)
        # if count==len(ransomNote): return True 
        # else: return False
        
        
        if len(magazine)<len(ransomNote):
            return False
        for r in set(ransomNote):
            if magazine.count(r)<ransomNote.count(r):
                return False

        return True 
        
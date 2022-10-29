class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res=[]
        for i in queries:
            for j in dictionary:
                if len(i)==len(j):
                    cnt=0
                    for char in range(len(i)):
                        if i[char]!=j[char]:
                            cnt+=1
                if cnt<=2:
                    res.append(i)
                    break                        
        return res
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2= len(s1),len(s2)
        counts1 = Counter(s1)
        for i in range(l2 - l1 + 1):
            counts2=Counter(s2[i:i+l1])
            if counts1 == counts2:
                return True
        return False
                
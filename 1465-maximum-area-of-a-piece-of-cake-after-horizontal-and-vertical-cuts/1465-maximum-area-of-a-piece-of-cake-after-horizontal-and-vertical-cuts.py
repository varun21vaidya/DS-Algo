class Solution:
    def maxArea(self, h: int, w: int, hori: List[int], ver: List[int]) -> int:
        hori.append(0)
        hori.append(h)
        ver.append(0)
        ver.append(w)
        hori.sort()
        ver.sort()
        l=0
        b=0
        for i in range(len(hori)):
            if(l<hori[i]-hori[i-1]):
                l=hori[i]-hori[i-1]
        for j in range(len(ver)):
            if (b<ver[j]-ver[j-1]):
                b=ver[j]-ver[j-1]
        return l*b%(10**9 + 7)
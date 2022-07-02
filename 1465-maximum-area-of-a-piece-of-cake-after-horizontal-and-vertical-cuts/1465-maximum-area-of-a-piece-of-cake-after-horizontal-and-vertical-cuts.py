class Solution:
    def maxArea(self, h: int, w: int, hori: List[int], ver: List[int]) -> int:
        
        
#       so here we will assume 0 and h to be limitations for vertical height
#       and 0 and w to be limitations for horizontal width
#       so we will append them as cuts in respective cut arrays
#       and then suppose array becomes (after sorting) for first eg h = 5, w = 4
#       horizontalcuts= [0,1,2,4,5]
#       verticalcuts = [0,1,3,4]
#       now in each array we will calculate max diff to get max width and max height
#       and then calculate area and take modulo of 10^9 + 7

        hori.append(0)
        hori.append(h)
        ver.append(0)
        ver.append(w)
        hori.sort()
        ver.sort()
        l=0
        b=0
        for i in range(len(hori)):
            l=max(l,hori[i]-hori[i-1])
        for j in range(len(ver)):
            b=max(b,ver[j]-ver[j-1])
        return l*b%(10**9 + 7)
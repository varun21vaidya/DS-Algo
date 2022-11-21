class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         low,high,count,maxx=0,0,0,0
#         sett=set()
#         n=len(s)
#         while high<n:
#             if s[high] in sett:
#                 maxx=max(maxx,high-low)
#                 # print(s[high],maxx)
#                 while s[high] in sett:
#                     sett.discard(s[low])
#                     low+=1

#             sett.add(s[high])

#             high+=1
#         return max(maxx,high-low)

        mapp={}
        l,maxx=0,0
        for r in range(len(s)):
            if s[r] in mapp:
                l=max(l,mapp[s[r]]+1)
            mapp[s[r]]=r
            maxx=max(maxx, r-l+1)
        return maxx
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low,high,count,maxx=0,0,0,0
        sett=deque()
        n=len(s)
        while high<n:
            if s[high] in sett:
                maxx=max(maxx,high-low)
                # print(s[high],maxx)
                while s[high] in sett:
                    low+=1
                    sett.popleft()

            sett.append(s[high])

            high+=1
        return max(maxx,high-low)
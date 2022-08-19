class Solution:
    def minWindow(self,s, t):
        mapp = Counter(list(t))
        count = sum(mapp.values())
        res = len(s)
        resMap = {}
        i = j = 0
        while j < len(s):
            if s[j] in mapp:
                if mapp[s[j]] > 0:
                    count -= 1
                mapp[s[j]] -= 1

            if count == 0:
                res = min(j-i, res)
                resMap[j-i] = s[i:j+1]
                while count <= 0:
                    if s[i] in mapp:
                        if mapp[s[i]] == 0:
                            count += 1
                            mapp[s[i]] += 1
                            i += 1
                            break
                        mapp[s[i]] += 1
                    i += 1
                    res = min(j-i, res)
                    resMap[j-i] = s[i:j+1]
            j += 1
        if res in resMap:
            return resMap[res]
        else:
            return ""
                
                
            
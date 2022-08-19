class Solution:
    def minWindow(self,s, t):
        
        
# create map for t string
# create count variable namedfor tracking total sum of occarances
# sliding window starts with i,j till j reaches end
# main condition: if s[j] is in map? then reduce count and value from map also increase j 
# if count becomes zero we have got potential solution 
# so store that in saperate map and keep length of it as key
# this key will help to keep solution minimum
# now as we have got a sliding window, but it may contain duplicate or redundant characters
# so move i till it still satifies our main condition 
# which is a potential substring with count=0
# so if s[i] is in map then and if its value is zero in map,
# it was not duplicate ie without it out condition may fail
# so increase count and its value in map ie while moving ahead with j we will need that character
# if its value is not zero then it is surely negative 
# which means with j its value became negative in map in main conditoin, as its duplicate
# then also we have to increase its value in map as we came across it
# else s[i] is not in map so we ignore it
# so atlast in any condition 
# we have to increase i, check minimum res and store current substring
# so if we have minimum value in map we will return its substring else empty string


        if len(s) < len(t):
            return ""
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
                
                
            
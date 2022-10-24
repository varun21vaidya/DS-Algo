class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
#       TC: 2^N, SC: 2^N
        maxarr=['']
        maxlen=0
        def isvalid(temp):
            return len(temp)==len(set(temp))
        for word in arr:
            for ele in maxarr:
                res=word+ele
                if isvalid(res):
                    maxarr.append(res)
                    maxlen=max(maxlen,len(res))
        return maxlen
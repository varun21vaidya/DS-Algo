class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter={}
        for i in arr:
            counter[i]=counter.get(i,0)+1
        counted=dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        # print(counted)
        totallen=len(arr)
        res=0
        remaining=totallen
        for i in counted:
            remaining=remaining-counted[i]
            # print(i, counted[i], remaining)
            res+=1
            if remaining<=totallen//2:
                return res
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if len(intervals)==1: return intervals
        res=[]
        intervals=sorted(intervals,key= lambda x : x[0])
        for i in range(len(intervals)):
            if not res or intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
                # print(res)
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
        return (res)
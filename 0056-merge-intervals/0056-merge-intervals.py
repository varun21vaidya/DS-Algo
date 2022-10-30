class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # if interval size is 1 directly return same intervals array
        if len(intervals)==1: return intervals
        
        # create a res array and sort the intervals according to start digit
        res=[]
        intervals=sorted(intervals,key= lambda x : x[0])
        
        # traverse through intervals and if there is no interval add in res
        # also check if start of current interval is less than previous interval 
        # if not then add current interval to res array
        # if yes then this previous interval will be updated with current intervals
        # but its start will be as it is as we had already sorted it
        # so update the end value with max of current intervals end and last intervals end
        # return the res array
        for i in range(len(intervals)):
            if not res or intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
                # print(res)
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
        return (res)
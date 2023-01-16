class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # corner case, of empty intervals
        if not intervals: return [newInterval]
        
        insertion=False
        
        # add the insertion at sorted position
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                insertion=True
                break
          
        # if newinterval not added,add it to last
        if not insertion: intervals.append(newInterval)
            
        
        # if last value of intervals added is greater than first value of next ele
        # update last value of intervals, else just append the new interval.
        new=[]
        for i in range(len(intervals)):
            if new and intervals[i][0]<=new[-1][1]:
                new[-1][1]=max(intervals[i][1], new[-1][1])
            else:
                new.append(intervals[i])

        return new
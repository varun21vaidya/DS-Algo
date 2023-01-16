class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        n=len(intervals)
        for i in range(n):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                break
        if len(intervals)==n: intervals.append(newInterval)
        # print(intervals)
        
        new=[]
        for i in range(len(intervals)):
            if new and intervals[i][0]<=new[-1][1]:
                new[-1][1]=max(intervals[i][1], new[-1][1])
            else:
                new.append(intervals[i])
        #     print(i,new)
        # print("------------------------------------")
        return new
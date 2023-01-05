class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: return 0
        points.sort(key = lambda k : k[1] )
        print(points)
        maxreach,arrow= points[0][1],1
        for i in range(1,len(points)):
            if points[i][0]>maxreach:
                arrow+=1
                maxreach=points[i][1]
        return arrow
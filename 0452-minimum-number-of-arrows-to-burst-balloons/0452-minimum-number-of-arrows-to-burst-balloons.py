class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        # Explanation:
        # so we will sort the array according to max ending of each ballon
        # ie end point ie 1st index
        # now we will assign maxreach varaible to traverse and 
        # check if any ballon goes out of its reach to shoot arrow
        # if yes increament arrow counter, and update maxreach to current ballons end 
        if not points: return 0
        points.sort(key = lambda k : k[1] )
        # print(points)
        maxreach,arrow= points[0][1],1
        for i in range(1,len(points)):
            if points[i][0]>maxreach:
                arrow+=1
                maxreach=points[i][1]
        return arrow
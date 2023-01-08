class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def calculate(x1,y1,x2,y2):
            if x1==x2: return float('inf'),float('inf')
            m=(y2-y1)/(x2-x1)
            b=y1-(m*x1)
            return m,b
        
        # we will store slope and b in hashmap
        # and if its already present increase its count
        result=1
        for i in range(len(points)):
            mapp=Counter()
            max_points=1
            for j in range(i+1, len(points)):
                (x1,y1),(x2,y2)=points[i],points[j]
                m,b=calculate(x1,y1,x2,y2)
                mapp[(m,b)]+=1
                max_points = max(max_points,1+ mapp[(m,b)])
            # print(mapp)
            result = max(result, max_points)
        return result


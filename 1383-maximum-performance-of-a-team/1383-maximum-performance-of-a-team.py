class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        maxx,curr,totalspeed =0,0,0
        que=[]
        for e,s in sorted(zip(efficiency,speed), reverse=1):
            if len(que)==k:
                slow=heapq.heappop(que)
                totalspeed-=slow
            heapq.heappush(que,s)
            totalspeed+=s
            curr=totalspeed*e
            maxx=max(maxx,curr)
        return maxx%(10**9+7)
    
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        h=[]
        N= len(costs)
        left=candidates
        right= N-candidates
        for i in range(left):
            heapq.heappush(h, (costs[i],i,1))
        for i in range(max(right,left),N):
            heapq.heappush(h,( costs[i],i,-1))
        right-=1
        print(h)
        total=0
        while k>0:
            cost,ind,dirr=heapq.heappop(h)
            total+=cost
            k-=1
            if left<=right:
                if dirr==1:
                    heapq.heappush(h, (costs[left],left,1))
                    left+=1
                else:
                    heapq.heappush(h, (costs[right],right,-1))
                    right-=1   
        
        return total
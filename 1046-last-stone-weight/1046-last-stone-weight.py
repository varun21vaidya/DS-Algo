class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        queue=[-x for x in stones]
        heapq.heapify(queue)
        while len(queue)>1:
            a,b=(-heapq.heappop(queue)),(-heapq.heappop(queue))
            if a-b!=0:
                temp=a-b
                heapq.heappush(queue,-temp)
        if queue: return -queue[0]
        else: return 0
                
        
        
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        from heapq import heapify, heappush, heappop
        piles= [-x for x in piles]
        heapify(piles)
        
        for _ in range(k):
            ele=-heappop(piles)
            heappush(piles,-(ele- ele//2))
            
        
        return -sum(piles)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
#         # intuation approach
#         if len(stones)==1:
#             return stones[0]
#         while len(stones)>1:
#             stones.sort()
#             if stones[-1]==stones[-2]:
#                 stones.pop()
#                 stones.pop()
#             else:
#                 temp=stones.pop()-stones.pop()
#                 stones.append(temp)
#             if len(stones)==0:
#                 return 0
#             if len(stones)==1:
#                 return stones[0]
            
            
        # Using Priority Queue 
        # but as python uses min priority que values are made negative
        
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
                
        
        
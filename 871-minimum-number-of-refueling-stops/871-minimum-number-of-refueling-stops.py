class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        #goto stations and fill when empty
        heap = []
        tank = startFuel
        stations.append([target,float("inf")])
        count = 0
        prev = 0
        
        for i in range(len(stations)):
            tank -= stations[i][0]-prev
            while heap and tank < 0:
                tank += -heapq.heappop(heap)
                count += 1
            if tank < 0:
                return -1
            heapq.heappush(heap,-stations[i][1])
            prev = stations[i][0]
        
        return count
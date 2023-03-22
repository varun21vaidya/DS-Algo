class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        #default dict graph with values as a list of [(dest, cost)]
        graph = defaultdict(list)
        for src, dest, cst in roads:
            graph[src].append((dest, cst))
            graph[dest].append((src, cst))
        #create heap and heapify, since 1 is the starting point
        heap = [graph[1]]
        heapq.heapify(heap)
        #result value
        minimum_cost = sys.maxsize
        #handle visited nodes
        visited = set()
        #add 1 as visited node
        visited.add(1)
        while heap:
            #pop
            edge = heapq.heappop(heap)
            #since it is a list of tuples, loop through them
            for i in edge:
                node, cst = i
                #find minimum cost
                minimum_cost = min(minimum_cost, cst)
                #if not visited, add to heap and repeat
                if node not in visited:
                    heapq.heappush(heap, graph[node])
                    visited.add(node)
        return minimum_cost
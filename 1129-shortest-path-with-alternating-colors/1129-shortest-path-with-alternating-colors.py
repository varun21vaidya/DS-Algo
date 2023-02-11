class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        redMap= collections.defaultdict(list)
        blueMap= collections.defaultdict(list)
        
        for src,destination in redEdges:
            redMap[src].append(destination)
        for src,destination in blueEdges:
            blueMap[src].append(destination)
            
        answer=[-1 for i in range(n)]
        q= deque() 
        q.append([0,0,None])# Node, distance, Previous Color
        visited = set() 
        visited.add((0,None))# Node, previous color
        
        while q:
            node, dist, prevColor = q.popleft()
            
            # if firsttime:
            if answer[node]==-1:
                answer[node]=dist
            
            if prevColor != "RED":
                for neighbour in redMap[node]:
                    if (neighbour,"RED") not in visited:
                        visited.add((neighbour, "RED"))
                        q.append([neighbour, dist+1,"RED"])
                    
            if prevColor != "BLUE":
                for neighbour in blueMap[node]:
                    if (neighbour,"BLUE") not in visited:
                        visited.add((neighbour, "BLUE"))
                        q.append([neighbour, dist+1,"BLUE"])
        
        
        return answer
        
        
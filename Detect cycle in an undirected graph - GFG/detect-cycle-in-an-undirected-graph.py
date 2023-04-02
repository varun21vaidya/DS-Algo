from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    

        # for handling various components, use a function 
        # for detecting a component has cycle or not
        # so even if one component has cycle, graph has cycle

        def detectCycle(src):
            q=deque([])
            q.append((src,-1))
            vis.add(src)
            while q:
                elem,source= q.popleft()
                
                for item in adj[elem]:
                    
                    # move only if item is not source
                    # ie dont return to where you came from
                    if item!=source:

                        # if item is in vis, we have already
                        # visited this item by some other direction
                        # ie this is part of cycle, return True
                        if item in vis:
                            return True

                        q.append((item,elem))
                        vis.add(item)
            return False

        
        vis=set()
        for i in range(V):
            if i not in vis:
                if detectCycle(i):
                    return True
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
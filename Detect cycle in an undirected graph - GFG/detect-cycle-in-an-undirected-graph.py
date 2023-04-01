from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	    
	    def detectCycle(src):
	        
    	    q= deque([])
    		vis.add(src)
    		q.append((src,-1))
    		
    		while q:
    		    elem, source= q.popleft()
    		    
    		    for item in adj[elem]:
    		        if item!=source:
    		            if item in vis:
    		                return True
    		            q.append((item,elem))
    		            vis.add(item)
    		            
    		            
    		return False
    		
    	vis=set()
    	for i in range(V):
    	    if i not in vis:
    	        if detectCycle(i)==True:
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
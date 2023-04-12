from collections import deque
class Solution:
	def isBipartite(self, V, adj):
		#code here
		
		# bfs mehtod
		
		def bfs(start):
    		q=deque()
    		q.append(start)
    		color[start]=0
    		
    		while q:
    		    elem= q.popleft()
    		    
    		    for item in adj[elem]:
    		        
    		        if color[item]==-1:
    		            color[item]=not color[elem] # opposite color of original color
    		            q.append(item)
    		            
    		        elif color[item]==color[elem]: # # if color is already there and its same as adjecent return False
    		            return False
    		      
            return True
            
        
	    color=[-1]*V  
	    for i in range(V):
	        if color[i]==-1:
                if not bfs(i): return False
        
        return True
	       
		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
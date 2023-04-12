from collections import deque
class Solution:
	def isBipartite(self, V, adj):

        def bfs(start, color):

            q = deque()
            q.append(start)

            while q:
                node = q.popleft()

                for item in adj[node]:

                    if color[item] == -1:
                        color[item] = not color[node]
                        q.append(item)

                    elif color[item] == color[node]:
                        return False

            return True


        def dfs(node, clr):
            color[node] = clr

            for item in adj[node]:
                if color[item] == -1:
                    if not dfs(item, not clr):
                        return False

                elif color[item] == color[node]:
                    return False

            return True

        # define a color array to maintain the track of colors of each node
        # if two adjecent nodes have same color return False
        color = [-1]*V

        # to handle multiple components we use a for loop and traversal.
        # if any node has -1 its not traversed yet so run traversal through it.

        for i in range(V):
            if color[i] == -1:
                # if not bfs(i,color): return False
                if not dfs(i, 0):
                    return False

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
#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        # shortest path
        # in bfs pop each node and traverse though each neighbour and get min distance
        # return the array of min dist
        
        adj=[[] for _ in range(n)]

        for v,it in edges:
            adj[it].append(v)
            adj[v].append(it)

        # bfs
        # q= deque([src])
        # dist=[float('inf')]*n
        # dist[src]=0

        # while q:
        #     node = q.popleft()
        #     for item in adj[node]:
                
        #         if dist[item]>dist[node]+1:
        #             dist[item]=dist[node]+1
        #             q.append(item)

        # for i in range(n):
        #     if dist[i]==float('inf'):
        #         dist[i]=-1

        # return dist
        
        # dfs
        def dfs(node):
            vis[node]=1
            
            for item in adj[node]:
                if dist[item]>dist[node]+1:
                    dist[item]=dist[node]+1
                if vis[item]==0:
                    dfs(item)
        
            vis[node]=0
        
        vis=[0]*n
        dist=[float('inf')]*n
        dist[src]=0
        for i in range(n):
            if vis[i]==0:
                dfs(i)
        
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        
        return dist
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends
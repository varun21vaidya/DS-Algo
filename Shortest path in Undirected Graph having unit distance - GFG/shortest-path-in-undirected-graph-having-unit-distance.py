#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        # shortest path
        # create adj list from edges
        # topo sort using bfs / dfs
        # if dfs pop each node and traverse though each neighbour and get min distance
        # return the array of min dist
        
        adj=[[]for _ in range(n)]

        for v,item in edges:
            adj[v].append([item,1])
            adj[item].append([v,1])
        # print(adj)
        
        q=deque()
        q.append(src)
        dist=[float('inf')]*n
        dist[src]=0
        
        while q:
            
            v = q.popleft()
             
            for item,wt in adj[v]:
                # dist[item]=min(dist[v]+wt, dist[item])
                if dist[item]>dist[v]+1:
                    dist[item]=dist[v]+1
                    q.append(item)
                
        for d in range(n):
            if dist[d]==float('inf'):
                dist[d]=-1
        
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
#User function Template for python3

from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        # BFS Using Kahn's Algorithm:
        indegree=[0]*V
        for v in range(V):
            for item in adj[v]:
                indegree[item]+=1
        # print(indegree)
        q=deque()
        res=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
                res.append(i)
                
        while q:
            node=q.popleft()
            for item in adj[node]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    res.append(item)

        # now we know that topo sort or Kahn's algo only works for Directed Acyclic Graph
        # so result would not have size of V if its cycle 
        return len(res)!=V
                
            
        
    
        # def dfs(start):
        #     vis[start]=2 # as its visited and path is continued
            
        #     for item in adj[start]:
        #         if vis[item]==0:
        #             if dfs(item): return True
                    
        #         elif vis[item]==2:
        #             return True
                
        #     vis[start]=1
        #     return False
    
        # # for multiple components
        # vis= [0]*V
        # # we will use marking like 
        # # for just visited but not on same path = 1
        # # for visited and on same path = 2
        
        # for i in range(V):
        #     if vis[i]==0:
        #         if dfs(i): return True
            
        # return False
        
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends
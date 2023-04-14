from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        # Kahn's Algorithm:
            
        # first calculate indegrees
        indegree=[0]*V
        for v in range(V):
            for item in adj[v]:
                indegree[item]+=1
        
        # print(indegree)
        
        # add zero degree vertices to queue
        res=[] # final sorted ans
        q= deque()
        for v in range(V):
            if indegree[v]==0:
                q.append(v)
                res.append(v)
                
        # BFS
        while q:
            node = q.popleft()
            
            for item in adj[node]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    res.append(item)
                
        # print(res)
        return res
        
        
        
        
        
        
        
        
        
        # def dfs(node):
        #     vis.add(node)
            
        #     for item in adj[node]:
        #         if item not in vis:
        #             dfs(item)
                
        #     stack.append(node)
            
            
            
    
        # vis=set()
        # stack=[]
        
        # for i in range(V): # 0 1 2... 8
        #     if i not in vis:
        #         dfs(i)
                
        # res=[]
        # for i in range(V):
        #     res.append(stack.pop())
            
        # return res


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends
#User function Template for python3
from collections import deque
from typing import List

class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        # code here
        # we will reverse the direction of pairs so terminal nodes become, indegreee
        # and the cycle part will not be considered in topo sort.
        
        revadj=[[] for _ in range(V)]
        for v in range(V):
            for item in adj[v]:
                revadj[item].append(v)
                
        indegree=[0]*V
        for v in range(V):
            for item in revadj[v]:
                indegree[item]+=1
            
        q=deque()
        res=[]
        for v in range(V):
            if indegree[v]==0:
                q.append(v)
                res.append(v)

        
        while q:
            node = q.popleft()
            for item in revadj[node]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    res.append(item)
                   
        res.sort() 
        return res
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        # def dfsCycle(node):
        #     vis[node]=2 # we are continuing same path

        #     for item in adj[node]:

        #         # if item is unvisited, traverse dfs and check if its cycle by checking if it returns true
        #         if vis[item]==0:
        #             if dfsCycle(item): return True

        #         # if vis[item] is 2 ie its on same path as node then both are in cycle
        #         if vis[item]==2:
        #             return True

        #     # rest that reach here are not part of cycle
        #     vis[node]=1
        #     return False

        # vis=[0]*V
        # safenodes=[]

        # for i in range(V):
        #     if vis[i]==0:
        #         dfsCycle(i)
                
        # for i in range(V):
        #     if vis[i]==1:
        #         safenodes.append(i)
        
        # return safenodes



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v = map(int, input().strip().split())
            adj[u].append(v)
        obj = Solution()
        ans = obj.eventualSafeNodes(V, adj)
        for nodes in ans:
            print(nodes, end = ' ')
        print()
            


# } Driver Code Ends
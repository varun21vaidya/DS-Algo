#User function Template for python3
from collections import deque
class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here

        # DAG: 
        
        # first convert this prerequisite into adj matrix
        
        # BFS for TOPOLOGICAL SORT ie KAHN's Algorithm
        q=deque()
        indegree=[0]*n # number of incoming paths for each vertices
        # print(indegree)
        adj=[[] for i in range(n)]
        for i , j in prerequisites:
            adj[j].append(i)
            indegree[i]+=1
            
        # print(adj)
        
        # first we have to append zero valued indegree vertices to queue and result
        result=[] # final order 
        
        for v in range(n):
            if indegree[v]==0:
                q.append(v)
                result.append(v)
    
        
        # run BFS
        while q:
            node = q.popleft()
            
            for item in adj[node]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    result.append(item)    
        if len(result)==n: return result
        else: return []
            

#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
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
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends
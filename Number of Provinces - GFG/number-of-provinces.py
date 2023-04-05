#User function Template for python3
from collections import defaultdict
class Solution:
    def numProvinces(self, adj, V):
        
        
        # dfs traversal
        def dfs(elem,adjList,vis):
            vis.add(elem)
            
            for x in adjList[elem]:
                if x not in vis:
                    dfs(x,adjList,vis)
        
        
        # code here 
        vis=set()
        # store to adj list
        adjList=[[]] # first list is just for initialization as nodes start from 1
        m=len(adj)
        n=len(adj[0])
        for i in range(m):
            adjList.append([])
            for j in range(n):
                if adj[i][j]==1 and i!=j: # self path not considered
                    adjList[i+1].append(j+1)
                
        # print(adjList)
        
        # loop for dfs
        count=0
        for i in range(1,len(adjList)):
            if i not in vis:
                dfs(i,adjList,vis)
                count+=1
                
        return count
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends
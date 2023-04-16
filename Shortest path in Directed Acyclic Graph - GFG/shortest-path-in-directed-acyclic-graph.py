#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        
        def dfs(node):
            vis.add(node)
            
            for it in adj[node]:
                item=it[0]
                if item not in vis:
                    dfs(item)
                    
            stack.append(node)
        
        
        adj=[[] for _ in range(n)]
        for v,it,wt in edges:
            adj[v].append([it,wt])
        # print(adj)
        
        vis=set()
        stack=[]
        
        for i in range(n):
            if i not in vis:
                dfs(i)
                
        res=[float('inf')]*n
        res[0]=0
        while stack:
            node=stack.pop()
            for item,wt in adj[node]:
                if res[item]>res[node]+wt:
                    res[item]=res[node]+wt
            
        for i in range(n):
            if res[i]==float('inf'):
                res[i]=-1
        
        return res
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends
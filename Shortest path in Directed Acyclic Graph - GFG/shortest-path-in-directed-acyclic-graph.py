#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        # now if the graph is acyclic graph, to calculate shortest distance
        # we will use TOPO Sort and after getting stack as in case of dfs, 
        # we will traverse and get minimum value for each item
        # ie compare existing dis value and value at current node + current wt
        # return the array with each item having shortest distance, 
        # if some item is non-rechable use -1

        # first convert edges into adjecent list
        
        adj=[[] for _ in range(n)]
        for v,item, wt in edges:
            adj[v].append([item,wt])

        # now calculate the topo sort
        def dfs(node):
            vis.add(node)
            for item in adj[node]:
                it = item[0]
                if it not in vis:
                    dfs(it)
            
            stack.append(node)

        vis=set()
        stack=[]
        for i in range(n):
            if i not in vis:
                dfs(i)


        distArr=[float('inf')]*n

        # distance from source to source is obviously zero
        distArr[0]=0

        while stack:
            node=stack.pop()

            for it,wt in adj[node]:
                if distArr[it]>distArr[node]+wt:
                    distArr[it]=distArr[node]+wt

        

        # if there are still dist unreachable ie infinity reset them to -1
        for i in range(n):
            if distArr[i]==float('inf'):
                distArr[i]=-1
        
        return distArr

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
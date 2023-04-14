#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        
        # as we need to depend on 1 task then another
        # this is similar to graph and especially topological sort
        # so logically if there are no cycles, we can complete tasks
        
        # def dfs(node):
        #     vis[node]=2
            
        #     for item in adj[node]:
        #         if vis[item]==0:
        #             if dfs(item): return True
                    
        #         if vis[item]==2:
        #             return True
                    
        #     stack.append(node)
        #     vis[node]=1
        #     return False

        # stack=[]
        # vis=[0]*N
        # adj=defaultdict(list)
        
        # # create adj list
        # for i,j in prerequisites:
        #     adj[i].append(j)
        # for node in range(N):
        #     if node not in adj:
        #         adj[node]=[]
        # print(adj)
        # # for i in range(N):
        # #     if vis[i]==0:
        # #         if dfs(i): return False
        # # # print(stack)   
        # # return True
                
                
        adj=defaultdict(list)
        
        # create adj list
        for i,j in prerequisites:
            adj[i].append(j)
        for node in range(N):
            if node not in adj:
                adj[node]=[]
        # print(adj)

                
        indegree=[0]*N
        for i,j in prerequisites:
            indegree[j]+=1
        
        # print(indegree)
        
        q=deque()
        count=0
        
        for d in range(N):
            if indegree[d]==0:
                q.append(d)
                count+=1
                
        while q:
            v= q.popleft()
            for item in adj[v]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    count+=1
                
        
        return count==N
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends
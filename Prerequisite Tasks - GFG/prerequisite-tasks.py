#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def isPossible(self,N,prerequisites):
        #code here
        
        # as we need to depend on 1 task then another
        # this is similar to graph and especially topological sort
        # so logically if there are no cycles, we can complete tasks
        
        # first create adjecency list 
        adj=[[] for i in range(N)]
        for i , j in prerequisites:
            adj[i].append(j)
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
#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        alph = dict()
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for l in range(K):
            alph[alphabets[l]]=l
        # print(alph)
        
        adj=[[] for _ in range(K)]
        
        # create adj list
        for i in range(1,N):
            letter, maxlen=0,min(len(alien_dict[i-1]),len(alien_dict[i]))
            
            while letter<maxlen:
                if alien_dict[i-1][letter]!=alien_dict[i][letter]:
                    # print(alien_dict[i-1][letter],"-->",alien_dict[i][letter])
                    adj[alph[alien_dict[i-1][letter]]].append(alph[alien_dict[i][letter]])
                    break
                letter+=1
            
        # print(adj)
            
        
        bfs=[]
        indegree=[0]*K
        q=deque()
        
        # populate indegree
        for v in range(K):
            for item in adj[v]:
                indegree[item]+=1
        
        for v in range(K):
            if indegree[v]==0:
                q.append(v)
        
        # print(indegree)
        while q:
            
            node = q.popleft()
            bfs.append(node)
            for item in adj[node]:
                indegree[item]-=1
                if indegree[item]==0:
                    q.append(item)
                    
        # print(bfs)
        ans=[]
        for i in range(K):
            ans.append(alphabets[bfs[i]])
        # print(ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
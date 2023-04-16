#User function Template for python3
from collections import defaultdict,deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        # if you observe that we have to decode the alien dictionary
        # by comparing with our letters, first K letters of our alphabetes are to be used
        # now when you observe [baa, abcd, abca ] you can tell that b should be before a , d before a like this pairs
        # so it seems familiar with topological sort and these pairs are indexes and K letters are vertices
        # So first create a string of our own alphabets
        # then we will create a hashmap with K letters and their index, which will be easy to operate graph


        # now if its topological sort, we will need to create an adjecent list
        # so we will traverse in this alien dictionary and compare the words
        # now when the word letters are not same then first word letter will have higher priority in sort
        # eg for abcd and abca, d and a are diff but abcd is earlier in list so d-->a like this create adj list
        # then you can use dfs or bfs.

        alphabets="abcdefghijklmnopqrstuvwxyz"
        hashmap=dict()
        adj=[[] for _ in range(K)]

        for i in range(K):
            hashmap[alphabets[i]]=i
        
        # print(hashmap)
        
        for word in range(1,N):
            letter, maxlen= 0, min(len(alien_dict[word-1]),len(alien_dict[word]))

            while letter<maxlen:
                if alien_dict[word-1][letter]!=alien_dict[word][letter]:
                    adj[hashmap[alien_dict[word-1][letter]]].append(hashmap[alien_dict[word][letter]])
                    break
                letter+=1
        
        # print(adj)

        bfs=[] # list to store the topological sort of indexs
        q=deque()

        indegree=[0]*K
        
        # populate the indegree
        for v in range(K):
            for item in adj[v]:
                indegree[item]+=1
        
        # get zero indegree nodes
        for v in range(K):
            if indegree[v]==0:
                q.append(v)
        
        # start bfs loop
        while q:
            node = q.popleft()
            bfs.append(node)
            for item in adj[node]:
                indegree[item]-=1

                if indegree[item]==0:
                    q.append(item)

        # print(bfs)

        # convert the index into letters again
        res=[]
        for i in range(K):
            res.append(alphabets[bfs[i]])
            
        # print(res)
        return res


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
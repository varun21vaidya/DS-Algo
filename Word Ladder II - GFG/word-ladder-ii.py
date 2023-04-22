#User function Template for python3

class Solution:
    def findSequences(self, start, end, wordList):
        
        from collections import deque
    	wordlist= set(wordList)
    	q =deque()
    	q.append([start, [start]])
    	alphabets="abcdefghijklmnopqrstuvwxyz"
    	res=[]
    	while q:
    		temp=[]
    		for _ in range(len(q)):
    			word, lst = q.popleft()
    			
    			if word == end:
    				res.append(lst)
    				continue
    			
    			for ind  in range(len(word)):
    				for letter in alphabets:
    					new = word[:ind]+letter+word[ind+1:]
    					if new in wordlist:
    						temp.append(new)
    						q.append([new, lst+[new]])
    			
    		for newword in temp:
    			wordlist.discard(newword)
    					
        return res


#{ 
 # Driver Code Starts
from collections import deque 
import functools

def comp(a, b):
    x = ""
    y = ""
    for i in a:
        x += i 
    for i in b:
        y += i
    if x>y:
        return 1
    elif y>x:
        return -1 
    else:
        return 0

if __name__ == '__main__':
    T=int(input())
    for tt in range(T):
        n = int(input())
        wordList = []
        for i in range(n):
            wordList.append(input().strip())
        startWord = input().strip()
        targetWord = input().strip()
        obj = Solution()
        ans = obj.findSequences(startWord, targetWord, wordList)
        if len(ans)==0:
            print(-1)
        else:
            ans = sorted(ans, key=functools.cmp_to_key(comp))
            for i in range(len(ans)):
                for j in range(len(ans[i])):
                    print(ans[i][j],end=" ")
                print()

# } Driver Code Ends
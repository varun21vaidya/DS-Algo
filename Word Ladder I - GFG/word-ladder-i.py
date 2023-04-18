class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		#Code here
		
		
		def bfs():
		    
		    q=deque()
		    q.append([startWord,1])
		    
		    while q:
		        word,count= q.popleft()
		        if word==targetWord:
		            return count
		          
	            for ind in range(len(word)):
	                for letter in alphabets:
	                    newWord=word[:ind]+letter+word[ind+1:]
	                    if newWord in wordlist:
	                        wordlist.discard(newWord)
	                        q.append([newWord,count+1])
	                        
            return 0
            
		alphabets="abcdefghijklmnopqrstuvwxyz"
		wordlist=set(wordList)

		return bfs()
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
        # def dfs(word,count,ind):
    
        #     if ind>=len(word):
        #         ind=0
        #     print(word,count)
        #     if word==targetWord:
        #         return count
            
        #     usedlater=word
        #     for letter in alphabets:
        #         if word[ind]==targetWord[ind]:
        #             return dfs(word,count,ind+1)
        #         if letter!=word[ind]:
        #             x= word[:ind]+letter+word[ind+1:]
        #             if x in vis: 
        #                 return dfs(x,count,ind+1)
        #             if x in wordList:
        #                 vis.add(x)
        #                 return dfs(x,count+1,ind+1)
                        
        #     return dfs(usedlater,count,ind+1)
        
        # alphabets="abcdefghijklmnopqrstuvwxyz"            
        # vis=set()
        # return dfs(startWord,1,0) 
    


#{ 
 # Driver Code Starts
from collections import deque 
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
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends
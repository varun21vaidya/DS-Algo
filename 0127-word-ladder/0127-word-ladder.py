class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordlist=set(wordList)
        q=deque()
        q.append([beginWord,1])
        wordlist.discard(beginWord)
        # alphabets="abcdefghijklmnopqrstuvwxyz"
        alphabetsSet=set()
        for words in wordlist:
            for letters in words:
                alphabetsSet.add(letters)
        alphabets="".join(alphabetsSet)
        # print(alphabets)
        
        while q:
            
            word,count= q.popleft()
            
            if word==endWord:
                return count
            
            for ind in range(len(word)):
                for letter in alphabets:
                    
                    newWord= word[:ind]+letter+word[ind+1:]
                    
                    if newWord in wordlist:
                        q.append([newWord,count+1])
                        wordlist.discard(newWord)
                    
        return 0
        
                    
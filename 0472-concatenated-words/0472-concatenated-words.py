class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        hashset= set()
        for w in words: hashset.add(w)
            
        def concatwords(word):
            
            for i in range(1, len(word)):
                prefix=word[:i]
                suffix=word[i:]
                
                if prefix in hashset and (suffix in hashset or concatwords(suffix)):
                    return True
        
        return [w for w in words if concatwords(w)]
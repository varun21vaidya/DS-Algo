class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # # Method 1:
        
        # if word==word.lower() or word==word.upper():
        #     return True
        # if word==word[0].upper()+word[1:].lower():
        #     return True
        # return False
        
        # # Method2:
        # if word.isupper() or word.islower() or word.istitle():
        #     return True
        # return False
    
        # # Method 3:
        return len(word)==1 or word[1:].islower() or word.isupper()
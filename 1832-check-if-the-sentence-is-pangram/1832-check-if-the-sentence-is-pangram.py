class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
#         s=set(sentence)
#         if len(s)==26:
#             return True
#         return False
        
        mapp={}
        for i in sentence:
            if i in mapp:
                continue
            else:
                mapp[i]=True
            
        return len(mapp)==26
    
        
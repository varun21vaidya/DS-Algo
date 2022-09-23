class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
#         letters="abcdefghijklmnopqrstuvwxyz"
#         letter=list(letters)
#         morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#         getmorse=dict(zip(letter,morse))
#         sett=set()
#         for word in words:
#             s=""
#             for i in word:
#                 s+=getmorse[i]
#             sett.add(s)
#         # print(sett)
#         return(len(sett))
                
    
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        sett=set()
        for word in words:
            s=""
            for i in word:
                s+=morse[ord(i)-97]
            sett.add(s)
        # print(sett)
        return(len(sett))
                
                
            
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score=maxx=0
        i,j=0, len(tokens)-1
        tokens.sort()
        while i<=j:
            if i==len(tokens)-1 and tokens[i]>power:
                return score
            elif tokens[i]<=power:
                power-=tokens[i]
                i+=1
                score+=1
            elif tokens[i]>power:
                if score>0:
                    power+=tokens[j]
                    j-=1
                    score-=1
                else: break
            maxx=max(maxx,score)
        return maxx
        
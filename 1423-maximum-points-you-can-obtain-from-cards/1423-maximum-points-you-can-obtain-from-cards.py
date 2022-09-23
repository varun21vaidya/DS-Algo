class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left, right = k-1, len(cardPoints)-1
        currsum=sum(cardPoints[:k])
        maxsum=currsum
        
        for _ in range(k):
            currsum+=cardPoints[right]-cardPoints[left]
            maxsum=max(currsum,maxsum)
            left,right=left-1, right-1
            
        return maxsum
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count=0
        if low and low%2==1:
            low-=1
        if high and high%2==1:
            high+=1
        return (high-low)//2
    
        
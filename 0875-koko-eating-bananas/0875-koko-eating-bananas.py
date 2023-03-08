class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            
            return sum(math.ceil(pile / speed) for pile in piles) <= h 

        
        low,high=1,max(piles)
        while low<high:
            mid=low+ (high-low)//2
            if check(mid):
                high=mid
            else:
                low=mid+1
            
        return low

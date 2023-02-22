class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # i th pile has piles[i] banana, max h hours are given 
        # so in this time we have to complete our eating
        # she can eat at max one pile so max speed could be max(piles)
        

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

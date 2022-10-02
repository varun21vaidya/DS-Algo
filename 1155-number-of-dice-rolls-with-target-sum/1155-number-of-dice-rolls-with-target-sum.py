class Solution:
           
    # Recursive Solution with pythons cache improvization 
    
    @lru_cache(maxsize=None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n==1:
            # if remaining target is within range of dice
            # which can be satisfied by last dice, then its one of ans
            if target<=k and target>0:
                return 1
            else: return 0

        count=0
        for i in range(1,k+1):
            count+=self.numRollsToTarget(n-1,k,target-i)

        return count%(10**9+7)
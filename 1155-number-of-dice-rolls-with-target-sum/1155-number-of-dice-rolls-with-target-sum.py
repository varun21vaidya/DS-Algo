class Solution:
            
    @lru_cache(maxsize=None)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if n==1:
            if target<=k and target>0:
                return 1
            else: return 0

        count=0
        for i in range(1,k+1):
            count+=self.numRollsToTarget(n-1,k,target-i)

        return count%(10**9+7)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp={}
        for i,v in enumerate(nums):
            if v in mapp:
                if i-mapp[v]<=k:
                    return True
            mapp[v]=i
        return False
        
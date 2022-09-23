class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res,pre=0,0
        mapp={}
        mapp[0]=1
        for i in nums:
            pre+=i
            if pre-k in mapp:
                res+=mapp[pre-k]
        
            mapp[pre]= mapp.get(pre,0)+1
        
        return res
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        def subarraySum(nums,k):
        
            res,pre=0,0
            mapp={}
            mapp[0]=1
            for i in nums:
                pre+=i
                if pre-k in mapp:
                    res+=mapp[pre-k]

                mapp[pre]= mapp.get(pre,0)+1

            return res
        
        
        r,c=len(matrix),len(matrix[0])
        ans=0
        for x in range(r):
            total=[0]*c
            for y in range(x,r):
                for j in range(c):
                    total[j]+=matrix[y][j]
                    
                ans+=subarraySum(total,target)
        
        return ans
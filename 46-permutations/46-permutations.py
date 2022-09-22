class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(temp,mapp):
            if len(temp)==len(nums):
                return res.append(temp[:])
                
            for i in nums:
                if not mapp[i]:
                    temp.append(i)
                    mapp[i]=1   
                    helper(temp,mapp)
                    x=temp.pop()
                    mapp[x]-=1
                    
        
        temp,mapp=[],{i:0 for i in nums}
        res=[]
        helper(temp,mapp)
        return res
        
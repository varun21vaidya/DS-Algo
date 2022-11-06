class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        
        # mapp=dict()
        # for i in nums:
        #     if i not in mapp:
        #         mapp[i]=1
        #     else:
        #         mapp[i]+=1
        #         if mapp[i]>n//2:
        #             break
        # return i
        
        # return sorted(nums)[n//2]
        
        candidate =0
        count= 0
        
        for value in nums:
            if count==0:
                candidate=value
            if candidate==value:
                count+=1
            else: 
                count-=1
        return candidate
        
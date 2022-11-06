class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # mapp=dict()
        n=len(nums)
        # for i in nums:
        #     if i not in mapp:
        #         mapp[i]=1
        #     else:
        #         mapp[i]+=1
        #         if mapp[i]>n//2:
        #             break
        # return i
        
        return sorted(nums)[n//2]
        
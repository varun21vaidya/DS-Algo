class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        mapp=dict()
        for i in nums:
            if i not in mapp:
                mapp[i]=1
            else:
                mapp[i]+=1
        # print(mapp)
        return [key for key,value in mapp.items() if value>n//3]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp={}
        for i in range(len(nums)):
            if nums[i] in mapp:
                return [i, mapp[nums[i]]]
            mapp[target-nums[i]]=i
            
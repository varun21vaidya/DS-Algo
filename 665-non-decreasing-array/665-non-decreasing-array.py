class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if flag or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False
                flag = 1
        return True
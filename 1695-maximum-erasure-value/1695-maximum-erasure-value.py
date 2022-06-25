class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # max_sum = 0
        # seen = set()
        # for l in range(len(nums)):
        #     seen.clear()
        #     curr_sum = 0
        #     r = l
        #     while r < len(nums):
        #         if nums[r] in seen:
        #             break
        #         curr_sum += nums[r]
        #         seen.add(nums[r])
        #         r += 1
        #     max_sum = max(max_sum, curr_sum)
        # return max_sum
        
        seen = set()
        curr_sum, max_sum, l = 0, 0, 0
        for num in nums:
            while num in seen:
                curr_sum -= nums[l]
                seen.remove(nums[l])
                l += 1
            curr_sum += num
            seen.add(num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
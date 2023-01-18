class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        totalSum = 0
        currMaxSum = 0
        currMinSum = 0
        maxSum = -math.inf
        minSum = math.inf

        for a in nums:
          totalSum += a
          currMaxSum = max(currMaxSum + a, a)
          currMinSum = min(currMinSum + a, a)
          maxSum = max(maxSum, currMaxSum)
          minSum = min(minSum, currMinSum)

        return maxSum if maxSum < 0 else max(maxSum, totalSum - minSum)
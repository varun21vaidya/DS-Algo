class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        # # brute force TLE
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] < nums[j] < nums[k]:
        #                 return True
        # return False
    
        # OPTIMAZTION FOR O(n) and constant space
        i, j = float('inf'), float('inf')
        for digit in range(len(nums)):
            if nums[digit]<=i:
                i=nums[digit]
            elif nums[digit]<=j:
                j=nums[digit]
            else:
                return True
        
        return False
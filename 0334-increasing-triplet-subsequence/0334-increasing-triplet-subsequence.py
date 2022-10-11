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
        
#         we will traverse through nums array and give smallest elemeent as i
#         if next element is large will get assigned to j and 
#         if its small again assigned to i, as we need smaller element for i
#         if both of them are full and further greater element occurse 
#         it means we got solution, return True
    
#         if doesnt return after loops means its either same elements or decreasing 
#         so return False
        
        i, j = float('inf'), float('inf')
        for digit in range(len(nums)):
            if nums[digit]<=i:
                i=nums[digit]
            elif nums[digit]<=j:
                j=nums[digit]
            else:
                return True
        
        return False
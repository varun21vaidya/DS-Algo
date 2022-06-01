class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Approach:
        # [1,3,4,2,2] og array
        # as we traverse label those negative
        # and if occured again 
        
        for i in nums:
            if nums[abs(i)]<0:
                return abs(i)
            else:
                nums[abs(i)]*=-1
                
#         def recursiveput(nums,nex):
#             if nex==nums[nex]:
#                 return nex
#             backed=nums[nex]
#             nums[nex]=nex
#             return recursiveput(nums,backed)
            
            
#         return recursiveput(nums,0)

        
            

            
            
class Solution:
    def threeSum(self, nums):
        res=[]
        nums.sort()
#         use 3 pointers left, mid, and right
#         left will be upto len(nums)-2, mid in middle and right will travel from end to mid
        
        for left in range(len(nums)-2):
            # we want to avoid duplicate combinations
            # so for arr= -2 -1 0 1 1 2 3 4
            # if left is is on 1 and in next iteration it again comes to 1 which will be unnecessary
            # so we will skip such condition, but for left=0 there is no previous
            if left>0 and nums[left]==nums[left-1]:
                continue
                
            mid=left+1
            right=len(nums)-1
            
            # iterate loop and traverse mid and right for this left
            while mid<right:
                summ= nums[left]+nums[mid]+nums[right]
                
                # as array is already sorted we can do some calculations based on sum
                # ie if summ is less than zero mid has to move to right to increase its value
                # and if summ is greater than 0 decrease right
                
                if summ<0: mid+=1
                    
                elif summ>0: right-=1
                    
                else: # means summ is 0 then append values and search for new values
                    res.append([nums[left],nums[mid],nums[right]])
                    
                    # as we skipped duplicates for left we have to do that for mid and right also
                    while mid< right and nums[mid]==nums[mid+1]:
                        mid+=1
                    while mid<right and nums[right]==nums[right-1]:
                        right-=1
                        
                    # traverse mid and right for next summ
                    mid+=1
                    right-=1
                    
        return res
                        
                
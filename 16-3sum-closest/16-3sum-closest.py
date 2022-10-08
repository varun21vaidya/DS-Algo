class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        
        for left in range(len(nums)-2):
            if left>0 and nums[left]==nums[left-1]:
                continue
            mid,right=left+1, len(nums)-1
            
            while mid<right:
                summ=nums[left]+nums[mid]+nums[right]
                
                if summ==target: return summ
                if abs(summ-target) <abs(closest-target):
                    closest=summ
                    
                if summ<target:
                    mid+=1
                elif summ>target:
                    right-=1
                else:
                    break

                
        return closest
                
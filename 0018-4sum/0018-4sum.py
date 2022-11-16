class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        nums.sort()
        for first in range(len(nums)-3):
            if first>0 and nums[first]==nums[first-1]:
                continue
            for second in range(first+1,len(nums)-2):

                # if second>0 and nums[second]==nums[second-1]:
                #     continue
                
                third,fourth=second+1,len(nums)-1
                
                while third<fourth:
                    
                    summ=nums[first]+nums[second]+nums[third]+nums[fourth]
                    if summ>target:
                        fourth-=1
                        
                    elif summ<target:
                        third+=1
                        
                    else:
                        res.add((nums[first],nums[second],nums[third],nums[fourth]))
                        # while third<fourth and nums[third]==nums[third+1]:
                        #     third+=1
                        # while third<fourth and nums[fourth]==nums[fourth-1]:
                        #     fourth-=1

                        third+=1
                        fourth-=1
                    
        return res
                    
                    
                
        
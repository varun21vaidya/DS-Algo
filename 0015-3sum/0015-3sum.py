class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        N=len(nums)
        for left in range(N-2):
            mid,right=left+1,N-1
            # print([nums[left] , nums[mid] , nums[right]])
            if left>0 and nums[left]==nums[left-1]:
                continue
            while mid<right:
                summ=nums[left] + nums[mid] + nums[right]
                # print(summ)
                if summ>0:
                    right-=1
                elif summ<0:
                    mid+=1
                else:
                    res.append([nums[left] , nums[mid] , nums[right]])
                    while mid<right and nums[mid]==nums[mid+1]:
                        mid+=1
                    while mid<right and nums[right]==nums[right-1]:
                        right-=1
                    mid+=1
                    right-=1
                    
        return res
                
        
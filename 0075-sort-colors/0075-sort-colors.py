class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         # counting sort (2 passes ie O(N)+O(N))
#         red,white=0,0
#         for i in nums:
#             if i==0: red+=1
#             elif i==1: white+=1
                
#         for i in range(len(nums)):
#             if red>0:
#                 red-=1
#                 nums[i]=0
#             elif white>0:
#                 white-=1
#                 nums[i]=1
#             else:
#                 nums[i]=2
                
        
        # Dutch National Flag Algorithm (1 pass O(N))
        low,mid,high =0,0,len(nums)-1
        
        while mid<=high:
            if nums[mid]==0:
                nums[mid],nums[low]=nums[low],nums[mid]
                mid+=1
                low+=1
            elif nums[mid]==2:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
            else:
                mid+=1
        
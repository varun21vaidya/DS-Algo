class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merged(nums1, nums2):
            i,j=0,0
            nums=[]
            while (i<len(nums1) and j<len(nums2)):
                if nums1[i]<nums2[j]:
                    nums.append(nums1[i])
                    i+=1
                else:
                    nums.append(nums2[j])
                    j+=1

            if i<len(nums1):
                nums+=nums1[i:]
            elif j<len(nums2):
                nums+=nums2[j:]
                
            return nums
        
        if (len(nums1)==0 or len(nums2)==0):
            nums=nums1+nums2
        else:
            nums=merged(nums1, nums2)
            
        mid=len(nums)//2  
        if len(nums)%2==0:
            median=(nums[mid]+nums[mid-1])/2
        else:
            median=nums[mid]
        
        return median
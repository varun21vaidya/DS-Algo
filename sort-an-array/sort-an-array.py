class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesorted(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left=mergesorted(nums[:mid])
            right= mergesorted(nums[mid:])
            return merge(left,right)
            
        def merge(left,right):
            m,n=len(left),len(right)
            i,j=0,0
            arr=[]
            while i<m and j<n:
                if left[i]<right[j]:
                    arr.append(left[i])
                    i+=1
                else:
                    arr.append(right[j])
                    j+=1
            
            arr+=left[i:]
            arr+=right[j:]
            return arr
           
        arr=[]    
        return mergesorted(nums)
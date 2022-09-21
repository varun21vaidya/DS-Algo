class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        evens= sum(ele for ele in nums if ele%2==0)
        for i in range(len(nums)):
            j=queries[i][1]
            # to replace next even if occured we need to replace current even 
            # so if here is even number subtract it from evens sum    
            if nums[j]%2==0: evens-=nums[j]
            nums[j]=nums[j]+queries[i][0]
            # and if now it contains even number add it to evens sum
            if nums[j]%2==0: evens+=nums[j]
            ans.append(evens)
        return ans
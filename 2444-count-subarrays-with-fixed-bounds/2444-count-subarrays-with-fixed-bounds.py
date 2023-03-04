class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
#         count=0
#         for num1 in range(len(nums)):
#             isMin,isMax=False,False
#             for num2 in range(num1, len(nums)):
#                 if nums[num2]==minK:
#                     isMin=True
#                 if nums[num2]==maxK:
#                     isMax=True
#                 if nums[num2]>maxK:
#                     break
#                 if nums[num2]<minK:
#                     break
#                 if isMin and isMax:
#                     count+=1
#         return count
        
        # Improving our Brute Force Solution:
        
        # first we have to do it in linear time complexity (one loop)
        # so how can we add and reset subarrays?
        # we can use a variable to check if subarray has any invalid number
        # we will initialize minInd and maxInd as representatives that
        # subarray contains  minK   and  maxK , so we will store their latest indexes. 
        # now we will have minInd and MaxInd for latest minK and maxK, and we will check 
        # which of them occurs first 
        # and then check if invalid index is greater than that, min of (minInd, maxInd)
        # if its greater than that, then subarray has invalid number hence ignore it
        # else if invalid index is less than min of both, then its out of subarray
        # and the from that invalid index to min of both, the other indexes can be starting points
        # ie the min of both will be our last starting point and diff between min of both and invalid
        # will be number of subarrays for that index
        # so it will indicate that the more starting points results in more subarrays
        # so it will give count of that many subarrays
        # so for each index, we will increase that subarray count, and return the result.
        
        minInd, maxInd, invalid= -1, -1, -1
        count=0
        for ind in range(len(nums)):
            if not minK<=nums[ind]<=maxK:
                invalid=ind
                
            if nums[ind]==minK:
                minInd=ind
                
            if nums[ind]==maxK:
                maxInd=ind
            
            lastStart= min(minInd,maxInd)
        # invalid index is less than min of both, then its out of subarray, so its valid subarray
            if invalid < lastStart:
                count+=lastStart-invalid
                
        return count
                    
            
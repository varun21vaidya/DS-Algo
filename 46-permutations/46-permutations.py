class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
# #         first of all we need a temp arr to store each permutation
# #         and we will also need a way to keep track of which number is already in temp
# #         so we will use map to check if its in temp arr or not
        
# #         so when we add a number in temp we will set its map value to 1
# #         and after recursions we will reduce it to 0 when we pop from temp
        
# #         so flow will be as follows
# #         before that define base case which will be 
# #         if the len of temp is equal to input arr, its a permutation
# #         now we will loop through each number to check if its in temp arr using mapp
# #         if its not there append it to temp, and set its value in map as 1
# #         then to append the next set of digits call recursion with updated temp and mapp
# #         when all numbers are added base condition will be satisfied
# #         store that permutation and return to exit that recursion call
# #         for next permutation we will need to rearrange the digits 
# #         so pop the recent digit and set its value as 0 in mapp
        
# #         now this loop will continue and recursion will move 
# #         and we will get all permutations
        
        
#         # TC: O(n!*n) permutations and loop
#         # SC: O(n) to store the temp arr
#         def helper(temp,mapp):
#             if len(temp)==len(nums):
#                 return res.append(temp[:])
                
#             for i in nums:
#                 if not mapp[i]:
#                     temp.append(i)
#                     mapp[i]=1   
#                     helper(temp,mapp)
#                     x=temp.pop()
#                     mapp[x]-=1
                    
        
#         temp,mapp=[],{i:0 for i in nums}
#         res=[]
#         helper(temp,mapp)
#         return res




#         now we can also solve this question without using extra map
#         instead we can just swap the digits in nums arr
#         for each level we will asign an index with which other digits will be swapped
#         and to swap all these index with specified index 
#         we will loop from that index to len of nums
#         and after each swap call recursively for next level of index
        
#         now when these index will cross the len of nums we will store that permutation
        
#         and imp that we also hava to reswap after each recursion 
#         like we used to do pop from the temp arr after recursion
        
        def helper(ind,nums):
            if ind>=len(nums):
                # print(nums)
                res.append(nums.copy())
                return
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                helper(ind+1,nums)
                nums[ind],nums[i]=nums[i],nums[ind]
        
        res=[]
        helper(0,nums)
        return res
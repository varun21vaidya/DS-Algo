# so as this problem contains the structure of array of digits leading to target sum
# so similar to subsequnce problems we can use recursion
# with adding a number calculate with recursion if its included in any subsequence 
# then removing the same number and calculating recursion for matching subsequences 
# without that number both conditions with increasing index untill lenght of original array

# now for this problem we are allowed to use same number unlimited times
# so we have to remember that we have to include same number in recursion
# by keeping the same index
# but to avoid the infinite loop, we have to reduce the target with that number
# and also check if that number is still less than target
# cz if target become less than current number, it will become negative

# now we have tried adding the same number few times now 
# if the target value is equal to zero, we will add the temp arr ie subsequence
# to the resultant array which will give output

# but if the target becomes less than current value,
# we will avoid further recursion with that number and increase index
# but before that remember to remove the element after previous recursion ended

# so recursion will flow like this
# first declare global result array
# call the function with temp= empty array and ind=0 along with arr and target

# if the base condition ie ind is equal to len(arr)
# and target becomes zero (as we are reducing target in recursion)
# copy of temp will be stored in result array

# the value at index if less than target will be added to temp
# and use recursion with target - that value and keep index same
# now after all those inside recursions when the recursion ends 
# remove the last added value 
# and use recursion for next index 

# at the end return the result array


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(ind, arr, target, temp,final):
            # base condition
            if ind == len(arr):
                if target==0:
                    # print("inserted",temp)
                    final.append(temp[:])
                return

            if arr[ind]<=target:
                temp.append(arr[ind])
                # print(temp)
                helper(ind, arr, target-arr[ind], temp,final)
                temp.pop()
                # print("popped",temp)
            helper(ind+1, arr, target, temp,final)
        
        final=[]
        helper(0, candidates, target, [],final)
        return final

 
        
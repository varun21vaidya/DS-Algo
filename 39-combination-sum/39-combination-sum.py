class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def helper(ind, arr, target, temp,final):
            # base condition
            if ind == len(arr):
                if target==0:
                    # print("inserted",temp)
                    final.append(temp[:])
                return final

            if arr[ind]<=target:
                temp.append(arr[ind])
                # print(temp)
                helper(ind, arr, target-arr[ind], temp,final)
                temp.pop()
                # print("popped",temp)
            helper(ind+1, arr, target, temp,final)
        
        global final
        final=[]
        helper(0, candidates, target, [],final)
        return final

 
        
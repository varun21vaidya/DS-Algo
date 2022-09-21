class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def helper(ind, arr, res, temp):
            if ind >= len(arr):
                if temp[:] not in res:
                    res.append(temp[:])
                return
            temp.append(arr[ind])
            helper(ind+1, arr, res, temp)
            temp.pop()
            helper(ind+1, arr, res, temp)

        ind, res, temp = 0, [], []
        nums.sort()
        helper(ind, nums, res, temp)
        return res
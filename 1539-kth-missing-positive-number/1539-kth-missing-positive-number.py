class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        sett= set(arr)
        res=0
        counter=0
        nums=0
        while not res:
            nums+=1
            if nums not in sett:
                counter+=1
            if counter==k:
                res=nums
        return res
        
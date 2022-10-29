class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        order= sorted(range(len(plantTime)), key= lambda x: -growTime[x])
        print(order)
        res,curr=0,0
        for i in order:
            curr+=plantTime[i]
            res= max(res, curr+growTime[i])
        return res
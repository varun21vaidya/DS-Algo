class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        order= sorted(zip(growTime,plantTime),reverse=True)
        # print(order)
        res,curr=0,0
        for grow,plant in order:
            curr+=plant
            # print(res, curr, grow)
            res=max(res,curr+grow)
        return res

from collections import deque
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sorted(properties, key = lambda k: k[1])
        # print()
        properties.sort(key=lambda x:(-x[0],x[1]))
        # print(properties)
        weak=0
        maxdef=properties[0][1]
        for att,defe in properties:
            if defe<maxdef:
                weak+=1
                continue
            else:
                maxdef=defe
        return weak
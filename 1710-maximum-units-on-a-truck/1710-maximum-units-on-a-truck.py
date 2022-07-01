class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
#       First sort the 2D array according to the maximum numberOfUnitsPerBox to get max total
        container=sorted(boxTypes, key=lambda box: box[1],reverse=True)
        total=0
        # print(container)
        for box in container:
            if truckSize-box[0]>0:
                total+=box[0]*box[1]
                truckSize-=box[0]
                # print(truckSize,total)
            else:
                if box[0]-truckSize>=0:
                    total+=(truckSize)*box[1]
                    return total

        return total     
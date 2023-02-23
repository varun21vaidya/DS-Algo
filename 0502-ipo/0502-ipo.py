class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        j,n=0,len(profits)
        sortedInput=list(zip(capital,profits))
        sortedInput.sort()
        h=[]
        while k>0:
            while j<n and w>=sortedInput[j][0]:
                heapq.heappush(h,-sortedInput[j][1])
                j+=1
            if not h:
                return w
            w+=-heapq.heappop(h)
            k-=1
        
        return w
            
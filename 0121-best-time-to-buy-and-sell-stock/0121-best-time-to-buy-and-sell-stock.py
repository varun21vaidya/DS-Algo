class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxx=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         maxx=max(maxx,prices[j]-prices[i])
        # return maxx
        
        currmin,maxx=float('inf'),0
        for i in range(len(prices)):
            currmin=min(currmin, prices[i])
            # print(prices[i],currmin)
            maxx= max(maxx, prices[i]-currmin)
        return maxx
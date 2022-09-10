class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # as we can do unlimited transactions
        # instead of taking and calculting local maxima, minima
        # we will just take diff between today and yesturday 
        # if its positive, its profit
        
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstbuy= secondbuy=float('inf')
        firstbuysell= secondbuysell=0
        
        for stock in prices:
            firstbuy=min(firstbuy,stock)
            firstbuysell=max(firstbuysell, stock-firstbuy)
            secondbuy=min(secondbuy,stock-firstbuysell)
            secondbuysell=max(secondbuysell, stock-secondbuy)
        return secondbuysell
            
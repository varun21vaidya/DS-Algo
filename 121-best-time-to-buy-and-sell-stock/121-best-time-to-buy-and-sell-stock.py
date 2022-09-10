class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_value=max(prices)
        profit, maximum_profit=0,0
        for i in prices:
            minimum_value=min(minimum_value,i)
            profit=i-minimum_value
            maximum_profit=max(maximum_profit,profit)
        return maximum_profit
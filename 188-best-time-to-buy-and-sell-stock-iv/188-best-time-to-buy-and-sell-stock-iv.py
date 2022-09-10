class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        firstbuy= float('inf')
        firstbuysell=0
        buy=[firstbuy for i in range(k+1)]
        sell=[firstbuysell for i in range(k+1)]
        for stock in prices:
            for i in range(k):
                buy[i]=min(buy[i],stock-sell[i-1])
                sell[i]=max(sell[i], stock-buy[i])
        print(buy, sell)
        return sell[k-1]
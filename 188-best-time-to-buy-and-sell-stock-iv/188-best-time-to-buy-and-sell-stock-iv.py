class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # taking logic from Best Time to Buy and Sell Stock III
        # where we had to calculate for only 2 transactions
        # here we had to calculate for k transactions, so we made 2 arrays
        # which replaces firstbuysell which was used to track 1st transactions profit
        # and instead we use previous value from sell array to track that profit and
        # it will calculate max profits for k transactions from each iteration of prices
        firstbuy= float('inf')
        firstbuysell=0
        buy=[firstbuy for i in range(k+1)]
        sell=[firstbuysell for i in range(k+1)]
        for stock in prices:
            for i in range(k):
                buy[i]=min(buy[i],stock-sell[i-1])
                sell[i]=max(sell[i], stock-buy[i])
        # print(buy, sell)
        return sell[k-1]
    
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
#         # taking logic from Best Time to Buy and Sell Stock III
#         # where we had to calculate for only 2 transactions
#         # here we had to calculate for k transactions, so we made 2 arrays
#         # which replaces firstbuysell which was used to track 1st transactions profit
#         # and instead we use previous value from sell array to track that profit and
#         # it will calculate max profits for k transactions from each iteration of prices


#         firstbuy= float('inf')
#         firstbuysell=0
#         buy=[firstbuy for i in range(k+1)]
#         sell=[firstbuysell for i in range(k+1)]
#         for stock in prices:
#             for i in range(k):
#                 buy[i]=min(buy[i],stock-sell[i-1])
#                 sell[i]=max(sell[i], stock-buy[i])
#         # print(buy, sell)
#         return sell[k-1]
        
#         #to improve timecomplexity
#         #if k is greater than half of length of prices
#         #ie greater than each transaction as n/2 means every transaction (buy&sell) is counted
#         #it just means we can use all values, ie every transaction can be counted
#         #so it just means its same as Best Time to Buy and Sell Stock II
        
#         if k>=len(prices)//2:
#             minimum_value=max(prices)
#             profit, maximum_profit=0,0
#             for i in prices:
#                 minimum_value=min(minimum_value,i)
#                 profit=i-minimum_value
#                 maximum_profit=max(maximum_profit,profit)
#             return maximum_profit


#this is same as explained above just rearranged
        if k>=len(prices)//2:
            profit=0
            for i in range(1,len(prices)):
                if prices[i]>prices[i-1]:
                    profit+=prices[i]-prices[i-1]
            return profit
        
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
    
    
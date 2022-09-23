class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
#         # taking logic from Best Time to Buy and Sell Stock III
#         https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39611/Is-it-Best-Solution-with-O(n)-O(1)./242914
#         # where we had to calculate for only 2 transactions
#         # here we had to calculate for k transactions, so we made 2 arrays
#         # which replaces firstbuysell which was used to track 1st transactions profit
#         # and instead we use previous value from sell array to track that profit and
#         # it will calculate max profits for k transactions for each iteration of prices


#         firstbuy= float('inf')
#         firstbuysell=0
#         buy=[firstbuy for i in range(k+1)]
#         sell=[firstbuysell for i in range(k+1)]
#         for stock in prices:
#             for i in range(k):
#                 buy[i]=min(buy[i],stock-sell[i-1])
#                 sell[i]=max(sell[i], stock-buy[i])
#         return sell[k-1]
        
    
    
    
#         #to improve timecomplexity
#         #if k is greater than half of length of prices
#         #ie greater than each transaction as n/2 means every transaction (buy&sell) is counted
#         #it just means we can use all values, ie every transaction can be counted
#         #so it just means its same as Best Time to Buy and Sell Stock II
        
#         if k>=len(prices)//2:
#            profit=0
#            for i in range(1,len(prices)):
#                if prices[i]>prices[i-1]:
#                    profit+=prices[i]-prices[i-1]
#            return profit


#this is same as explained above just rearranged
#Time complexity, O(nk)
#Space complexity, O(nk)

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
        return sell[k-1]
    
    
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        # # Recursive
        
        # first we need to understand is, we need to calculate all paths for 
        # day 1 pass, day 7 pass and day 30 pass, now once we get that 
        # we need to increase the index
        # now if we take 7 day pass or 30 day pass, we will do one time pay
        # and for rest 6 days or 29 days we dont need, so increase index by that days
        # and for that keep a maxdays variable 
        # now after calculating all those for 1 day, 7 day and 30 day
        # just return min of them 


        # def solver(i,maxdays):
        #     if i>=len(days):
        #         return 0
            
        #     if days[i]<=maxdays:
        #         return solver(i+1, maxdays)

        #     day1=costs[0]+solver(i+1,days[i]+0)
        #     day7=costs[1]+solver(i+1,days[i]+6)
        #     day30=costs[2]+solver(i+1,days[i]+29)

        #     return min(day1,day7,day30)
        
        # return solver(0,0)



        # # MEMOIZATION

        # def solver(i,maxdays):
        #     if i>=len(days):
        #         return 0
            
        #     if days[i]<=maxdays:
        #         return solver(i+1, maxdays)

        #     if dp[i]!=0:
        #         return dp[i]

        #     day1=costs[0]+solver(i+1,days[i]+0)
        #     day7=costs[1]+solver(i+1,days[i]+6)
        #     day30=costs[2]+solver(i+1,days[i]+29)

        #     dp[i]= min(day1,day7,day30)
        #     return dp[i]
        
        # dp=[0 for i in range(len(days))]
        # return solver(0,0)


        # # Bottom Up Appoach: 

        # the max days we need to keep track is 365 days so 
        # either we can use max dp size of last day of array or 365
        # now we will take a range from first day to last day or 365 day of days array
        # and in that there will be days which are not present in array for those
        # just consider previous value and continue

        # for rest which are present we need to calculate 1day pass value, 7 day and 30 day
        # now for total cost of that pass = cost of travel before x days 
        #                                   + cost of travel of x days
        # ie for 1 day pass = dp[i-1]+ costs[0]
        # for 7 day pass = dp[i-7]+ costs[0]
        # for 30 day pass = dp[i-30]+ costs[0]
        # but as we are starting from 1 there will be i-1 =0 but for i-7 and i-30
        # that value will not be present hence we will check if its present 
        # and if not then we will consider it as 0

        # finally take the min of all of them and return ans

        dp=[0 for i in range(days[-1]+1)]
        daysset=set(days)
        for i in range(1,days[-1]+1):
            if i not in daysset:
                dp[i]=dp[i-1]
            else:
                day1=costs[0]+dp[i-1]
                day7=costs[1]+dp[max(0, i-7)]
                day30=costs[2]+dp[max(0,i-30)]

                dp[i]=min(day1,day7,day30)

        return dp[-1]
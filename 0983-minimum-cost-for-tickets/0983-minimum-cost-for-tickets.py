class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
#         def solver(ind,maxdays):
#             if ind>=len(days):
#                 return 0
#             if days[ind]<=maxdays:
#                 return solver(ind+1,maxdays)
                
#             x = min(solver(ind+1,days[ind]+0)+costs[0],
#                    solver(ind+1,days[ind]+6)+costs[1],
#                    solver(ind+1,days[ind]+29)+costs[2])
#             return x
        
#         return solver(0,0)


        def solver(ind,maxdays):
            if ind>=len(days):
                return 0
            if days[ind]<=maxdays:
                return solver(ind+1,maxdays)
                
            if dp[ind]!=-1:
                return dp[ind]
            dp[ind] = min(solver(ind+1,days[ind]+0)+costs[0],
                   solver(ind+1,days[ind]+6)+costs[1],
                   solver(ind+1,days[ind]+29)+costs[2])
            return dp[ind]
        
        dp=[-1 for i in range(len(days))]
        solver(0,0)
        # print(dp)
        return dp[0]
    
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # greedy
#         satisfaction.sort()
#         maxx=float('-inf')
        
#         def calc(satisfaction):
#             summ=0
#             for i in range(len(satisfaction)):
#                 summ+=(i+1)*satisfaction[i]
#             return summ
#         maxx=max(maxx,calc(satisfaction))
#         while satisfaction:
#             satisfaction.pop(0)
#             x=calc(satisfaction)
#             maxx=max(maxx,x)
        
#         return maxx

#         maxx=0
#         summ=0
#         satisfaction.sort(reverse=True)
#         for i in range(len(satisfaction)):

#             summ+=satisfaction[i]
#             if summ<0:
#                 return maxx
#             maxx+= summ
            
#         return maxx

#         def solver(ind,time):
#             if ind>=len(satisfaction):
#                 return 0
            
#             return max((satisfaction[ind]*time+solver(ind+1,time+1)), solver(ind+1,time))
        
#         satisfaction.sort()
#         return solver(0,1)


        def solver(ind,time):
            if ind>=len(satisfaction):
                return 0
            if (ind,time) in memo:
                return memo[(ind,time)]
            
            memo[(ind,time)]= max((satisfaction[ind]*time+solver(ind+1,time+1)), solver(ind+1,time))
            return memo[(ind,time)]
        
        memo=dict()
        satisfaction.sort()
        return solver(0,1)

            
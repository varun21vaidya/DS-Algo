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

        maxx=0
        summ=0
        satisfaction.sort(reverse=True)
        for i in range(len(satisfaction)):

            summ+=satisfaction[i]
            if summ<0:
                return maxx
            maxx+= summ
            
        return maxx
        
            
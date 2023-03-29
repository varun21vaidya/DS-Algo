class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # greedy
        satisfaction.sort()
        maxx=float('-inf')
        
        def calc(satisfaction):
            summ=0
            for i in range(len(satisfaction)):
                summ+=(i+1)*satisfaction[i]
            return summ
        maxx=max(maxx,calc(satisfaction))
        # print(maxx)
        while satisfaction:
            satisfaction.pop(0)
            # print(satisfaction)
            x=calc(satisfaction)
            # print(x)
            maxx=max(maxx,x)
        
        return maxx
            
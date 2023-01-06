class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans,i,n=0,0,len(costs)
        while coins>0 and i<n:
            if coins<costs[i]:
                break
            if coins>=costs[i]:
                coins-=costs[i]
                ans+=1
            i+=1
        return ans
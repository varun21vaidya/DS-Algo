class Solution:
    def profitableSchemes(self, N: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def dfs(i, p, n):
            if i == len(group):
                if p >= minProfit:
                    return 1
                return 0
            pick = 0
            if n - group[i] >= 0:
                pick = dfs(i + 1, min(minProfit, p + profit[i]), n - group[i])
            skip = dfs(i + 1, p, n)
            return pick + skip
        
        return dfs(0, 0, N) % (10 ** 9 + 7)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # def solve(w1, w2, i, j):
        #     if (i == L1 and j == L2):
        #         return 0
        #     if (i == L1 or j == L2):
        #         return max(L1 - i, L2 - j)
        #     if w1[i] == w2[j]: 
        #         return solve(w1, w2, i + 1, j + 1)                
        #     return 1 + min(solve(w1, w2, i + 1, j), solve(w1, w2, i, j + 1))
        # L1, L2 = len(word1), len(word2)
        # return solve(word1, word2, 0, 0)      
        
        #DP solution
        def solve(w1, w2, i, j):
            if i == len(w1) and j == len(w2) : return 0
            if i == len(w1) or j == len(w2) : return max(len(w1) - i, len(w2) - j)
            if dp[i][j] != 1000 : return dp[i][j]
            if w1[i] == w2[j] : 
                return solve(w1, w2, i + 1, j + 1)
            dp[i][j] = 1 + min(solve(w1, w2, i + 1, j), solve(w1, w2, i, j + 1))
            return dp[i][j]
        L1, L2, dp = len(word1), len(word2), [[1000]*(len(word2)+1) for i in range(len(word1)+1)]
        return solve(word1, word2, 0, 0)
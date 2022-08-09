class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        mapp, ans = defaultdict(), 0
        for num in arr:
            ways, limit = 1, sqrt(num)
            for factorA in arr:
                if factorA > limit: break
                factorB = num / factorA
                if factorB in mapp:
                    ways += mapp[factorA] * mapp[factorB] * (1 if factorA == factorB else 2)
            mapp[num], ans = ways, (ans + ways)
        return ans % 1000000007
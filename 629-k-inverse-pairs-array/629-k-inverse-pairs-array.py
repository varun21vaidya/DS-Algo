class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if n==0: return 0
        if k == 0 : return 1
        counter = [1] + [0 for i in range(k)]
        for j in range(1, n):
            new_count = [1] + [0 for i in range(k)]
            temp = 1
            for x in range(1, k+1):
                temp += counter[x]
                if x >= j+1:
                    temp -= counter[x-j-1] 
                new_count[x] = temp
            counter = new_count
        return counter[-1] % (1000000007)
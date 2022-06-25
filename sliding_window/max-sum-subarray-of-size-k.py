# Problem-link: https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1
# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum.

class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        i, j = 0, 0
        maxx, summ = 0, 0
        while j < N:
            summ += Arr[j]
            if j-i+1 == K:
                maxx = max(summ, maxx)
                summ -= Arr[i]
                i += 1
            j += 1
        return maxx


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N, K = input().split()
        N = int(N)
        K = int(K)
        Arr = list(map(int, input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K, Arr, N))
# } Driver Code Ends

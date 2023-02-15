class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def ZerosinArray(arr):
            return len([x for x in arr if x == 0])
        
        
        # # s1 s2 - sum of subset 1 and sum of subset 2
        # # s1+s2=sum(nums)=w
        # # s1-s2=target
        # # 2s1=w+target
        # # s1=(w+target)//2
        # # now we just have to find if any subset matches s1 sum
        # # rest is same as count of subset sum ie if we replace w with s1

        s1= (sum(nums)+target)
        if s1%2!=0 or s1<0: return 0   
        s1//=2
        n=len(nums)
        dp= [[0 for _ in range(s1+1)] for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(s1+1):
                # if i==0:
                #     dp[i][j]=0
                # if j==0:
                #     # dp[i][j] = 1
                #     # if 0 are present in array it will consider only 1 but it should consider {} and 0
                #     dp[i][j] = 2**ZerosinArray(nums[:i])
                    
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][s1]

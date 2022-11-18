#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, nums):
        #Code here
        mapp={}
        summ,maxx=0,0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ==0:
                maxx=max(maxx,i+1)
            elif summ in mapp:
                maxx=max(maxx,i-mapp[summ])
            else:
                mapp[summ]=i
        
        return maxx

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
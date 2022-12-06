#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        # ans=1
        # for i in range(1,n):
        #     count=1
        #     for j in range(i+1,n):
        #         if (arr[i]>=arr[j] and arr[i]<=dep[j]) or (arr[j]>=arr[i] and arr[j]<=dep[i]):
        #             count+=1
        #     ans=max(ans,count)
        # return ans
        
        arr.sort()
        dep.sort()
        count,maxx=1,0
        i,j=1,0
        while i<n and j<n:
            if arr[i]<=dep[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxx=max(count,maxx)
        return maxx
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends
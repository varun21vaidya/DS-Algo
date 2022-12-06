#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        x= [(start[i], end[i]) for i in range(n)]
        x= sorted(x, key= lambda k : k[1])
        # print(x)
        count=1
        last=x[0][1]
        for i in range(1,n):
            if last<x[i][0]:
                last=x[i][1]
                count+=1
        return count
            


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
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
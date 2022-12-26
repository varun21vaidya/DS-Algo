#User function Template for python3

class Solution:
    def numberOfPaths (self, n, m):
        if n==1 or m==1:
            return 1
        
        return self.numberOfPaths(n-1, m)+ self.numberOfPaths(n, m-1)
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        m, n = map(int, input().split())
        ans = ob.numberOfPaths(m, n)
        print(ans)




# } Driver Code Ends
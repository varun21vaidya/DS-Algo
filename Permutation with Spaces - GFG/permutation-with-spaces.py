#User function Template for python3

class Solution:
    def permutation (self, S):
        # code here
        def solver(S,ind,temp,N):
            if ind>=N:
                ans.append(temp)
                return
            
            res1= temp+S[ind]
            solver(S, ind+1, res1, N)
            
            res2= temp+" "+S[ind]
            solver(S, ind+1, res2, N)
        
        ans=[]
        N= len(S)
        solver(S, 1, S[0], N)
        ans.sort()
        return ans
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        S = input()
        ans = ob.permutation(S);
        write = "";
        for i in ans:
            write += "(" + i + ")"
        print(write)


# } Driver Code Ends
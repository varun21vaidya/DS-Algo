#{ 
 # Driver Code Starts
import math



# } Driver Code Ends
#Complete this function

class Solution:
    def josephus(self,n,k):
        #Your code here
        
        def kill(lst, k):
            
            n= len(lst)
            
            if n==1:
                return lst[0]
                
            if n<=k:
                ind=(k-1)%n
            else:
                ind=k-1
            
            recur= lst[ind+1:]+lst[:ind]
            return kill(recur, k)
           
        persons=[i+1 for i in range(n)]     
        return kill(persons,k)   


#{ 
 # Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(Solution().josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
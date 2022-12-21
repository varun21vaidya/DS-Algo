#User function Template for python3


class Solution:
    def reverse(self,st): 
        
        def insert(st,temp,maxx,count):
            if count==maxx:
                st.append(temp)
                return st
            val=st.pop()
            insert(st,temp,maxx,count+1)
            st.append(val)
        
        def rev(st, maxx):
            if maxx==0:
                return st
            top= st.pop()
            
            insert(st, top, maxx,0 )
            return  rev(st, maxx-1)
        
        return rev(st, len(st)-1)
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            ans=(ob.reverse(arr))
            for el in ans:
                print(el,end=" ")
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
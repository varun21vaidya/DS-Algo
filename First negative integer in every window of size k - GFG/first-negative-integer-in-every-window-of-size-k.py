#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    lst,res=[],[]
    i,j=0,0
    while j<N:
        if A[j]<0:
            lst.append(A[j])
        
        if j-i+1==K:
            # print(lst, res)
            if lst:
                res.append(lst[0])
                if A[i]==lst[0]:
                    lst.remove(A[i])
            else:
                res.append(0)
            i+=1
                
        j+=1
        
    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    
    
    # Approach:
    # So approach is to use sliding window
    # as we will traverse through array only once
    # we will collect each negative number in our iteration
    # and will return first value of temp list
    # as we want first negative number
    # and as we move past the window 
    # if current first value of temp list was in prsevious window
    # we will remove that value from temp list
    # and if temp list is empty for any window, will return 0
    
    lst,res=[],[]
    i,j=0,0
    while j<N:
        
        # first check if no is negative if yes,
        # append it to temp list
        if A[j]<0:
            lst.append(A[j])
        
        # check if window is endings
        # and then use 2 parts 
        # first for updating result ie negative value or 0
        # and next if current first value of temp list(lst[0]) is
        # not be present in next window
        # ie as we move i new window will be there 
        # so if A[i] is equal to lst[0] we will remove that value also
        # as its not going to be there in next window
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
#User function Template for python3

class Solution:
    def sortBySetBitCount(self, arr, n):
        # Your code goes here
        
        def countSet(num):
            count=0
            # x = bin(elem)[2:] #num =4 ==> 0b0100
            # for val in x:
            #     if val=="1":
            #         count+=1
            
            while num&(num-1)>0:
                count+=1
                num=num&(num-1)
            
            return count
                
            
        temp= []
        for elem in arr:
            temp.append([elem,countSet(elem)])

        sortedarray = sorted(temp,key = lambda k : k[1], reverse=True)
        arr[:] = [pair[0] for pair in sortedarray]
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends
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
        
        # print(temp)
        
        # n log n algo
        # def sort(array):
        #     if len(array)>1:
        #         mid= len(array)//2
        #         left= sort(array[:mid])
        #         right= sort(array[mid:])
            
        #         return mergesort(left, right)
                
        #     else:
        #         return array
            
        # def mergesort(left, right):
        #     a,b,m,n = 0,0,len(left), len(right)
        #     merge=[]
            
        #     while a<m and b<n:
        #         if left[a]<right[b]:
        #             merge.append(left[a])
        #             a+=1
        #         else:
        #             merge.append(right[b])
        #             b+=1
            
        #     merge.extend(left[a:])
        #     merge.extend(right[b:])
            
        #     return merge
            # sort(temp.keys()) sorted(temp.values())
        # sortedsets= sort(list(temp.values())) 
        # sortedarray= []
        
        sortedarray = sorted(temp,key = lambda k : k[1], reverse=True)
        arr[:] = [pair[0] for pair in sortedarray]
        
        return arr
        
        # for sortset in sortedsets:
        #     sortedarray.append(temp[sortset])
        
        # return sortedarray[::-1]
            
        

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
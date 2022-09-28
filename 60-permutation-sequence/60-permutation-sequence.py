class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        # # Recursion (GOT TLE)
#         def solver(ind,arr,res):
            
#             if ind==len(arr):
#                 res.append(arr.copy())
#                 return
#             for i in range(ind,len(arr)):
#                 arr[ind],arr[i]=arr[i],arr[ind]
#                 solver(ind+1,arr,res)   
#                 arr[ind],arr[i]=arr[i],arr[ind]   

            
#         arr=[i for i in range(1,n+1)]
#         temp,res=[],[]
#         solver(0,arr,res)
#         return "".join([str(i) for i in sorted(res)[k-1]])

        # define fact,numbers array
        fact=1
        nos=[]
        # calculate n-1 factorial
        for i in range(1,n):
            fact=fact*i
            nos.append(i)
        # append last numner
        nos.append(n)
        
        # if k is 17 in array of 0th index start we want k-1th ind ie 
        # to simplyfy we want k=k-1th number
        k=k-1
        
        # result to be stored
        ans=""
        
        while True:
                
            # r each fact part of numbers out of permutationn of nos array numbers
            # we have to get the k//fact the index array number
            # and add it to result
            
            ans= ans+ str(nos[k//fact])
            
            # now after addding it to ans, we have to get for remaining nums
            # so remove this one form nos array
            
            nos.remove(nos[k//fact])
            
            # limiting condition           
            if len(nos)==0:
                break
            
            # out of remaining numbers of get index to add it to ans so recalculate k
            k=k%fact
            
            # update fact 
            fact=fact//len(nos)
            
        return ans
            
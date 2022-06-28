class Solution:
    def maxSlidingWindow(self, A: List[int], B: int) -> List[int]:
        
        
#       SO as we can imagine we have to find maximum as we slide through the window
#       and we can achieve by maintaining a maxx vairable and compairing it with each addition of j
#       and when window reaches k will append maxx to result array
#       but there is catch, what if maxx is first value of previous window,
#       ie as window moves we cant determine what will be next max, is it from remaining i to j 
#       ie remaining array or is new number added ie new j
#       so for that we need to store that info in some data structure 
#       so we use double sided queue, and its first value will be always max

        i,j,res=0,0,[]
        dq=deque()

        while j<len(A):
            
            # if new element is greater than previous elements
            # then now we dont need previous elements
            # as until this becomes the element to be removed, its lower elements 
            # ie next numbers will be next maxx which will be added and until then this will be max
            # and everytime some greater number adds, previous numbers will be deprecated
            while dq and dq[-1]<A[j]:
                dq.pop()
            dq.append(A[j])
                
            # print(dq)
            
            if j-i+1==B:
                # the element at front will always be max element
                res.append(dq[0])
                
                
                # when the max element is first to be removed as window will slide, 
                # we will also pop that value from dq so, its next maxx will be at front of dq
                if dq[0]==A[i]:
                    dq.popleft()
                # print(res)
                i+=1
            j+=1
        
        return res
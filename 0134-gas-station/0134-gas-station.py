class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
       # Method 1: Brute Force O(N*N)
#         s=0
#         n=len(gas)
#         while s<n:
#             totalcost=gas[s]
#             for i in range(n):
#                 if totalcost<cost[(s+i)%n]:
#                     totalcost=-1
#                     break
#                 else:
#                     totalcost-=cost[(s+i)%n]
#                     totalcost+=gas[(s+i+1)%n]
#             if totalcost>=cost[(s+i+1)%n]:
#                 return s
#             s+=1
#         return -1
            
    
    # METHOD 2 : Linear TIME COMPLEXITY O(N)
    
        # lets create the diffences at each point
        # if its sum is negative, then surely we cant go to next station
        
        difference= [gas[i]-cost[i] for i in range(len(gas))]
        
        if sum(difference)<0:
            return -1
        
        # now we will traverse the array
        # and add the diff to total
        # if at any point total becomes negative,
        # we can be ensure that the required start point is not before this point
        # so move start ahead of this point ie i+1
        # and reset the total
        # finally return the start point
        
        
        start,i, total=0,0,0
        while i<len(gas): #Traversal 
            
            total+=difference[i]
            
            if total<0:
                start=i+1
                total=0
                
            i+=1
            
        return start
            
            
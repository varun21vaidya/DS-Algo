#User function Template for python3

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        # # sort according to max profits
        # # and place it according to deadline
        
        # # TC: O(nlogn + m*n) for sorting + looping
        
        # jobs=sorted(Jobs, key = lambda k : k.profit, reverse=True)
        # maxdead=0
        # for i in range(n):
        #     deadline=jobs[i].deadline
        #     maxdead=max(maxdead, deadline)
        
        # deadlines=[False for i in range(maxdead+1)]
        # work=0
        # done, prof=0,0
        # for work in range(n):
        #     limit=jobs[work].deadline
            
        #     # initially all deadline slots would be false
        #     # so as we have already sorted with max profit 
        #     # for that slot if its empty, we will get max profit job
        #     # and add it to resultant profit
            
        #     if not deadlines[limit]:
        #         deadlines[limit]=limit
        #         done+=1
        #         prof+=jobs[work].profit
        #     else:
                
        #         # if there is already a job present 
        #         # so we have to travel downwards towards lower deadline slot
        #         # and check if it is empty, and add it to profit,
        #         # then break and move to next work
        #         x=limit
        #         while x>0:
        #             if not deadlines[x]:
        #                 deadlines[x]=limit
        #                 done+=1
        #                 prof+=jobs[work].profit
        #                 break
        #             x-=1
        # return done, prof   
        
        # ****************************************************************************
        
        # Intuition:
        # we have to create a priority queue which stores the max profit jobs and if the seats are 
        # available pop that max profit element and add to total profit
        # but array should be sorted according to the deadline in descending order so max deadline 
        # jobs will be processed first and if next job has deadline different or lower than current, then 
        # it would indicate that current is last deadline which will fill that slot for deadline
        
        # eg if deadlines are 3,3,3,2,2,1,1 and if we are at 3rd iteration ie deadline 3 then, this 
        # shows this current deadline is last chance to fill the deadline slot for deadline 3
        # as next deadlines are 2,1,etc ie lower than it
        # so from priority queue we will pop the most profit job and can put it on slot 3
        # and add that profit to total.
        # so we have to make a slots variable which will determine if this is last deadline for that slot
        # ie this will be last position where we can choose element for that slot.
        
        # so if it is last position with that deadline ie next deadline is lower, add that many slots
        # to be available, and pop the max profit job from pq, and reduce the slot
        
        
        # SO ALGO will be as follows:
            
        # 1. first sort the array descending order to deadline
        # 2. use priority queue and add the current element in it
        # 3. check if its not last element and calculate the slots by taking diffence from next deadline
        # 4. if slots are available, pop the maxprofit job, add to total profit and reduce slot
        
        import heapq
        
        jobs= sorted(Jobs, key= lambda k : k.deadline, reverse=True)
        # for i in range(n):
        #     print(jobs[i].id,jobs[i].deadline,jobs[i].profit)
            
        done, totalprofit=0,0
        pq=[]
        slots=0
        
        for i in range(n):
            
            heapq.heappush(pq, -jobs[i].profit)
            
            if i!=n-1:
                slots=jobs[i].deadline-jobs[i+1].deadline
            else:
                slots=jobs[i].deadline
            
            while slots and pq:
                prof= heapq.heappop(pq)
                done+=1
                totalprofit+=-prof
                slots-=1
        
            
        return done, totalprofit
        

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
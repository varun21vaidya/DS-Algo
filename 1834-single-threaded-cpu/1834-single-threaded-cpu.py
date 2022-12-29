class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        taskheap= []
            
        # add index to tasks
        for i in range(len(tasks)):
            tasks[i]= [tasks[i][0],tasks[i][1],i]
        
        # sort it acc to enqueue time, so we can check
        # which are available at this moment, and only push those to minheap
        sortedtasks= sorted(tasks, key= lambda k : k[0])
        # print(sortedtasks)
        
        # to track available tasks
        totaltime=0
        
        res=[] # to store indexes
        
        # tracker will traverse through sortedtaks to check available tasks
        # and will push all tasks which are available
        tracker=0
        
        
        # first check if totaltime is equal to or greater than current tracking task
        # if not update totaltime to its enque time
        # eg at start, totaltime is 0 and if minimum element is starting at 4 enqueue time.
        
        # so run till we reach end of sortedtasks
        # according to our current ie minimum enqueueTime,
        # for that specific totaltime, push less than or equal to tasks to minheap

        
        # now we have available tasks in heap, which will sort tasks according to min process time
        # pop the element 
        
        while tracker<len(tasks) or taskheap:
            
            if not taskheap and totaltime<sortedtasks[tracker][0]:
                totaltime=sortedtasks[tracker][0]
             
            # print('totaltime',totaltime)
            # print("pushing tasks")
            while tracker<len(tasks) and totaltime>=sortedtasks[tracker][0]:
                # print(sortedtasks[tracker])
                heapq.heappush(taskheap,[sortedtasks[tracker][1],sortedtasks[tracker][2]])
                tracker+=1
               
            
            # print("popping tasks")
            popped= heapq.heappop(taskheap)
            totaltime+=popped[0]
            # print(popped)
            res.append(popped[1])  


        return res
        

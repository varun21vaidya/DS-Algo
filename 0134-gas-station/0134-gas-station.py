class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # we have to calculate the difference between gas and cost
        # which means if we can move ahead with current gas and required cost
        # so first calculate those values and store
        # then use two variables one to determine current sum and second for index
        
        arr=[]
        for i in range(len(gas)):
            arr.append(gas[i]-cost[i])
        if sum(arr)<0:
            return -1
        
        ind, summ=0,-1
        # now traverse with the arr,
        # to check if the diff of those gas is greater to complete the circle
        # if summ is -1, make ind=i
        # if summ plus current gas is greater than cost 
        # update summ
        # if summ is less than 0, make it -1
        # return pos
        for i,diff in enumerate(arr):
            if summ==-1: pos=i
            
            if summ+diff>=0:
                summ+=arr[i]
            else:
                summ=-1
                
        return pos
            
                
        
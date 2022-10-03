class Solution:
    def minCost(self, colors, arr):
        
        # Two Pointer Approach:
        left,right,totaltime=0,0,0
        currmax,currtotal=arr[left],arr[left]

        while right<len(arr):
            currmax,currtotal=0,0
            
            while right<len(arr) and colors[left]==colors[right]:
                    currmax=max(currmax,arr[right])
                    currtotal+=arr[right]
                    right+=1
            totaltime+=(currtotal-currmax)
            left=right

                
        return totaltime
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
#       Recursive Solution
#       Instead of making [1,1,1] into [9,3,5]
#       we will make 9,3,5 to 1,1,1
#       First take sum of array
#       take maximum value
#       then get diff of both
#       and subract that diff from maximum

#       to make things easy we will directly update with index
#       instead of using sort or direct using max

#       to improve efficiency use mod for updating arr[maxx]

        #summ is total of array and maxx is index of maximum value of array
        summ,maxx=0,0
        for i in range(len(target)):
            summ+=target[i]
            if target[i]>target[maxx]:
                maxx=i
        
        diff=summ-target[maxx]
        
        if target[maxx]==1: return True         #output
        if diff==1: return True                 #[1,5] diff will always be 1 so faster output
        if diff==0: return False                #[2]
        if diff>target[maxx]: return False      #[1,3,3]
        if target[maxx]%diff==0: return False   #[20,5]
            
        target[maxx]%=diff
        return self.isPossible(target)
        
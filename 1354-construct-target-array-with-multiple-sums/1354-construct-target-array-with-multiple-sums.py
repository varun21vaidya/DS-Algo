class Solution:
    def isPossible(self, target: List[int]) -> bool:
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
        
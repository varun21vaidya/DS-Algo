class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxL,maxR=[0]*n,[0]*n #left stack, right stack ie maxL, maxR
        maxL[0]=height[0]
        maxR[n-1]=height[n-1]
        for i in range(1,n):
            '''
            if maxL[i-1]>=height[i]:
                maxL[i]=maxL[i-1]
            else:
                maxL[i]=height[i]
            '''
            maxL[i]=max(maxL[i-1],height[i])
        
        for i in range(n-1,0,-1):
            '''
            if maxR[i]>=height[i-1]:
                maxR[i-1]=maxR[i]
            else:
                maxR[i-1]=height[i-1]
            '''
            maxR[i-1]=max(maxR[i],height[i-1])
                
        #print(maxL)
        #print(maxR)
        ans=0
        for i in range(n):
            ans+=min(maxL[i],maxR[i])-height[i]
        
        return ans
        
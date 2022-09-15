class Solution:
    def findOriginalArray(self, changed):
        
        #brute force (GOT TLE)
#         reflect=collections.Counter(changed)
        
#         res=[]
#         while reflect:
#             mini=min(reflect)
#             reflect[mini]-=1
#             if reflect[mini]==0: del reflect[mini]
#             if not reflect[mini*2]>0:
#                 return []
#             reflect[mini*2]-=1
#             res.append(mini)
#             if reflect[mini*2]==0: del reflect[mini*2]

#         if not reflect:
#             return res
#         else:[]




#       n*logK Solution

#         reflect=collections.Counter(changed)
#         if reflect[0]%2: return []
#         for i in sorted(reflect):
#             if reflect[i]>reflect[i*2]: return []
            
#             #for condition of even count of 0 we will need output of half of them
#             if not i:
#                 reflect[i*2]-=reflect[i]//2
#             else: #for all other numbers
#                 reflect[i*2]-=reflect[i]
            
#         return list(reflect.elements())
    
    
# BEST AND EASY TO UNDERSTAND:
        changed.sort()
        que=deque([])
        output=[]
        
        for i in changed:
            if que and que[0]==i:
                que.popleft()
            else:
                que.append(i*2)
                output.append(i)
        if que: return []
        return output
        
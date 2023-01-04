class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        mapp={}
        for i in range(len(tasks)):
            if tasks[i] not in mapp:
                mapp[tasks[i]]=1
            else:
                mapp[tasks[i]]+=1
        # print(mapp)
        
        ans=0
        for freq in mapp.keys():
            if mapp[freq]==1:
                return -1
            elif mapp[freq]%3==0:
                ans+=mapp[freq]//3
            else:
                ans+=mapp[freq]//3+1
        
        return ans
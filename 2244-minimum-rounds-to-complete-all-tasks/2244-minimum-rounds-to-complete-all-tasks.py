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
                # after using 3s there many be even number remaining whih will be handled by a 2 or there may be 1 remaining which will be handled by reducing one 3 and addding 2 
                # but any of them requires same count so extra one is used for handling with 2.
                ans+=mapp[freq]//3+1 
        return ans
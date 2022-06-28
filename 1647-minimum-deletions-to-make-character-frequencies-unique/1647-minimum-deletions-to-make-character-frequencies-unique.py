# class Solution:
#     def minDeletions(self, s: str) -> int:
#         mapp={}
#         for i in s:
#             mapp[i]=mapp.get(i,0)+1
#         print(mapp)
#         freq=list(mapp.values())
#         notseen=[]
#         print(freq)
#         cnt=0
#         for i in range(len(freq)):
#             print(i, freq[i])
#             if freq[i] in notseen:
#                 while freq[i]-1 in notseen and freq[i]>=0:
#                     freq[i]-=1
#                     cnt+=1
#                     if freq[i]<=0:
#                         break
#                 if freq[i]>0:
#                     freq[i]-=1
#                     cnt+=1
#             notseen.append(freq[i])
#             print(freq)
#         return cnt

class Solution:
    def minDeletions(self, s: str) -> int:
        mapp={}
        for i in s:
            mapp[i]=mapp.get(i,0)+1
        # print(mapp)
        freq=list(mapp.values())
        notseen=[]
        # print(freq)
        cnt=0
        for i in range(len(freq)):
            # print(i, freq[i])
            if freq[i] in notseen:
                while freq[i]-1 in notseen and freq[i]>=0:
                    freq[i]-=1
                    cnt+=1
                    if freq[i]<=0:
                        break
                if freq[i]>0:
                    freq[i]-=1
                    cnt+=1
            notseen.append(freq[i])
            # print(freq)
        return cnt
    
    
    
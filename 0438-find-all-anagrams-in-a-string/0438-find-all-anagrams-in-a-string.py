class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # # Brute Force - HASHMAP
        # countp=Counter(p)
        # res=[]
        # for i in range(len(s)-len(p)+1):
        #     new=Counter(s[i:i+len(p)])
        #     if new==countp:
        #         res.append(i)
        # return res
            
        # sliding window
        i,j,n=0,0, len(s)
        k=len(p)
        res=[]
        countp=Counter(p)
        temp={}
        while j<n:
            temp[s[j]]=temp.get(s[j],0)+1
            
            if j-i+1==k:
                if temp==countp:
                    res.append(i)
                temp[s[i]]-=1
                if temp[s[i]]==0:
                    del temp[s[i]]
                i+=1
                j+=1
            else:
                j+=1
                
        return res
                
            
            
            
        
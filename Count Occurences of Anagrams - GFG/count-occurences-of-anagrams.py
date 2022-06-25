#User function Template for python3
class Solution:
	def search(self,pat, txt):
	    i,j,res=0,0,0
	    mapp,patmap=dict(),dict()
	    for p in pat:
	        patmap[p]=patmap.get(p,0)+1
	   # print(patmap)
	    while j<len(txt):
	        mapp[txt[j]]=mapp.get(txt[j],0)+1
	        
	        if (j-i+1)==len(pat):
	            
	           # print(mapp)
	            if mapp==patmap:
	                res+=1
                mapp[txt[i]]-=1
                if mapp[txt[i]]==0: mapp.pop(txt[i])
	            i+=1
	        j+=1
	        
	    return res
	   

#{ 
#  Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends
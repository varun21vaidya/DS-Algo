#User function Template for python3
class Solution:
	def search(self,pat, txt):
	    
	    
	   # So one way was to calculate all anagrams of pat
	   # and find those in txt
	   # but calculting only anagram would be O(n!)
	    
	    
	   # Approach: Sliding Window
	   # As there is string, substring and fixed window(len of substring)
	   # we can use sliding window for this
	    
	   # so parts of sliding window:
	   # initialization, while loop, calculation part, condition and ans part
	    
	   # so here for each sliding window we can check which letters are present
	   # and are the number of each letters(count) same for window and pat
	   # if yes to both then its anagram of pat
	    
	   # so if we are considering count of strings we will use dictionary
	    
	   # so first we will create counted dictionary of pat
	   # now come to calulation part, for each sliding window we will 
	   # either update count by 1 or if its not there create count with default 0 +1
	    
	   # and in the ans part, if both dicitonaries are same increase result value
	   # and with each slide drop arr[i] from dictionary value and if its 0 remove it
	    
	    
	    #Initialization part
	    i,j,res=0,0,0
	    mapp,patmap=dict(),dict()
	    for p in pat:
	        patmap[p]=patmap.get(p,0)+1
	   # print(patmap)
	   
	   
	    #loop part
	    while j<len(txt):
	        
	        #calculation part
	        mapp[txt[j]]=mapp.get(txt[j],0)+1
	        
	        #condition part
	        if (j-i+1)==len(pat):
	            
	           # print(mapp)
	           
	            #ANS part
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
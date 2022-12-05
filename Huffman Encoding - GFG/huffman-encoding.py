#User function Template for python3
import heapq


class Solution:
    
    def huffmanCodes(self,S,f,N):
        
        class node:
            def __init__(self,val,symbol,left=None,right=None):
                self.val=val
                self.symbol=symbol
                self.left=left
                self.right=right
                self.huff=""
            def __lt__(self, nxt):
                return self.val < nxt.val
          
        res=[]  
        heap=[]
        
        # create a heap structure from characters
        for i in range(N):
            heapq.heappush(heap, node(f[i], S[i]))
            
        # while we get a root node at the end, we will pop 2 minheaps and merge them to get their root
        # and place this newnode with left and right as these two minheap nodes
        # in the process lable min1 and min2 with 0 and 1 as their huffman code
        while len(heap)>1:
            min1=heapq.heappop(heap)
            min2=heapq.heappop(heap)
            min1.huff=0
            min2.huff=1
            newnode= node(min1.val+ min2.val, min1.symbol+min2.symbol, min1, min2)
            heapq.heappush(heap, newnode)
        
        # print(heap[0].val)
        
        def gethuff(heap, huffval):
            newval=huffval+str(heap.huff)
            
            if heap.left:
                gethuff(heap.left,newval)
            # print(heap.val)
            if heap.right:
                gethuff(heap.right,newval)
                
            # we have reach the leaf nodes ie og characters
            if not heap.left and not heap.right:
                # print(heap.symbol,newval)
                res.append(newval)
                
        gethuff(heap[0], "")
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S= input()
		N= len(S);
		f= [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.huffmanCodes(S,f,N)
		for i in ans:
		    print(i, end = " ")
		print()
# } Driver Code Ends
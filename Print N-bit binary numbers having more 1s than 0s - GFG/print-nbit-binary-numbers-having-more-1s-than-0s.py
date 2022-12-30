#User function Template for python3
class Solution:
	def NBitBinary(self, N):
		# code here
		
		# find binary number of N bits
		# filter those numbers whose 1s are more than or equal to 0s
        # def printer(num, extra, remain):
        #     if remain==0:
        #         ans.append(num)
        #         return
            
        #     printer(num+"1", extra+1, remain-1)
            
        #     if extra>0:
        #         printer(num+"0", extra-1, remain-1)
                
                
        # strr=""
        # ans=[]
        # printer(strr, 0, N)
        # return ans
            
        
        # we can also apply generate balanced parenthesis logic
        # where instead of "(" and ")", we use '1'and '0'
        
        
        #     # first condition: total length will be n
        #     # so '1' will have maximum count of n
        #     # addition condition: for '1' :
        #     # 1 can be added untill its count is upto n,
        #     # and 0 can be added if count of '0' is less than '1'
        
        #     # temp: temp string to add to final result
        #     # ind: to count total length of string
        #     # count1: count of '1'
        #     # count2: count of '0'

        def solver(n,temp, count1,count2, ind):
            if ind>=n:
                ans.append(temp)
                return
            
            if count1<n:
                solver(n, temp+"1", count1+1,count2, ind+1)
                
            if count2<count1:
                solver(n, temp+"0",count1,count2+1,ind+1)
                
        ans=[]
        solver(n, "", 0,0,0)
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends
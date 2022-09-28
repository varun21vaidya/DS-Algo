class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        
# first of all we need to partition the string 
# at each index and then check string upto that index is palindrome or not
# if its palindrome then use recursion and check the partition for remaining string
# with updated index 
# to update index we need to loop through the string and each point repeat the process
# ie check for palindrome and use recursion, and remember to remove that after recursion
# as backtracking process.
# now when the index goes out of string we will have the partitioned array
# and append it to resultant array
        def ispali(s):
            return s==s[::-1]
        def solver(ind,s,temp,res):
            if ind==len(s):
                # print(temp)
                res.append(temp[:])
                return
            for i in range(ind,len(s)):
                
                if ispali(s[ind:i+1]):
                    temp.append(s[ind:i+1])
                    solver(i+1,s,temp,res)
                    temp.pop()
        temp,res=[],[]
        solver(0,s,temp,res)
        return res
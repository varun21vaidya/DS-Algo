class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # first condition: total length will be 2*a
        # so '(' will have maximum count of a, so as ')'
        # addition condition: for '(' :
        # ( can be added untill its count is upto a,
        # and ) can be added if count of ')' is less than '('
        
        # temp: temp string to add to final result
        # ind: to count total length of string
        # count1: count of '('
        # count2: count of ')'
        
        # base examples: 
        # for A=1 op: ()
        # for A=2 op: (()), ()()
        
        
        def solver(temp, ind, count1,count2):
            if ind>=2*n:
                ans.append(temp)
                return

            if count1<n:
                solver(temp+"(", ind+1, count1+1, count2)
            
            if count2<count1:
                solver(temp+")", ind+1, count1,count2+1)
                
        ans=[]
        solver("", 0,0,0)
        return ans
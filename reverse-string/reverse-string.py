class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def solver(s,ind):
            if ind==len(s)//2:
                return s
            s[ind],s[len(s)-1-ind]=s[len(s)-1-ind],s[ind]
            solver(s,ind+1)
            
        return solver(s,0)
            
        
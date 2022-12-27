class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def solver(s, temp, ind):
            
            if ind>=len(s):
                ans.append(temp)
                return

            if s[ind].isnumeric():
                solver(s, temp+s[ind], ind+1)
            else:
                solver(s, temp+s[ind], ind+1)
                solver(s, temp+(s[ind].swapcase()), ind+1)

        ans=[]
        solver(s, "", 0)
        return ans
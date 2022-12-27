class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def solver(s, temp, ind):
            if ind >= len(s):
                ans.add(temp)
                return
            
            if s[ind].isnumeric():
                temp += s[ind]
                ind += 1

            if ind >= len(s):
                ans.add(temp)
                return

            solver(s, temp+s[ind], ind+1)
            solver(s, temp+(s[ind].swapcase()), ind+1)

        ans = set()
        solver(s, "", 0)
        return ans
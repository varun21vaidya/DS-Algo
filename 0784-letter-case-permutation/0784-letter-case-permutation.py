class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def solver(s, temp, ind):
            
#             if ind < len(s):
#                 if s[ind].isnumeric():
#                     temp += s[ind]
#                     ind += 1

#             if ind >= len(s):
#                 ans.add(temp)
#                 return

#             solver(s, temp+s[ind], ind+1)
#             solver(s, temp+(s[ind].swapcase()), ind+1)

#         ans = set()
#         solver(s, "", 0)
#         return ans

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
class Solution:
    def lengthOfLongestSubstring(self, s):
        
        #using set
#         l=0
#         charset=set()
#         res=0
#         for r in range(len(s)):
#             while s[r] in charset:
#                 charset.remove(s[l])
#                 l+=1
#             charset.add(s[r])
#             res=max(res,r-l+1)
        
#         return res
                 
        #using dictionary
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
            
            
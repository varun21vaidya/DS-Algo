class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
#         n=len(palindrome)
        
#         # if its only any single letter we cant replace it still and make it non-palindrome
#         # so just return empty string
        
#         if n==1:
#             return ""
        
#         # to get lexographilcally smallest non palindrome
#         # we have to observe that it would be contain 'a' first
#         # but if its already have 'a' initially then 
#         # the next non-'a' would be replaced with 'a'
        
#         st=""
#         for i in range(n):
#             if palindrome[i]!='a':
#                 st+='a'
#                 st+=palindrome[i+1:]
#                 if st!=st[::-1]:
#                     return st
#                 else: break
#             st+=palindrome[i]
            
#         # but what if all are already 'a' 'aaaaaa'
#         # we need to change last letter with 'b' while still making it smallest lexographically
        
#         return palindrome[:-1]+'b'


        # WITHOUT EXTRA SPACE

        # instead of using extra space for 'st'
        # what was corner case was that 'aba'
        # when we changed b it became palindrome 'aaa'
        # so with using extra space we had to check if it was palindrom or not
        # but if we just check upto half of that string we could avoid that condition
        # as it will conclude either that if we traverse upto half and no change is there 
        # it means either whole string is 'aaaa' or middle character is non-'a'
        # in both case we have to change then last character only
        
        # so we can ignore the condition with just taking loop upto n//2-1
        # and remove that st and its palindrome check
        
        n=len(palindrome)
        
        if n==1: return ''
        
        for i in range(n//2):
            if palindrome[i]!='a':
                return palindrome[:i]+'a'+palindrome[i+1:]
           
        # if conditions are 'aabaa' or 'aaaa' change last character with b
        return palindrome[:-1]+'b'
            
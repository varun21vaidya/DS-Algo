class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n=len(palindrome)
        
        # if its only any single letter we cant replace it still and make it non-palindrome
        # so just return empty string
        
        if n==1:
            return ""
        
        # to get lexographilcally smallest non palindrome
        # we have to observe that it would be contain 'a' first
        # but if its already have 'a' initially then the next non-'a' would be replaced with 'a'
        
        st=""
        for i in range(n):
            if palindrome[i]!='a':
                st+='a'
                st+=palindrome[i+1:]
                if st!=st[::-1]:
                    return st
                else: break
            st+=palindrome[i]
            
        # but what if all are already 'a' 'aaaaaa'
        # we need to change last letter with 'b' while still making it smallest lexographically
        
        return palindrome[:-1]+'b'
class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def recurse(left,right):
            if left>=right:
                return 0
            
            elif s[left]==s[right]:
                return recurse(left+1,right-1)
            
            else:
                return 1+ min(recurse(left+1,right), recurse(left,right-1))
        
        
        return recurse(0,len(s)-1)
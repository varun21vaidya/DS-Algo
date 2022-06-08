class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s=="".join(reversed(s)):
            return 1
        return 2
            
class Solution:
    def longestPalindrome(self, s):
            pali = ''
            dp = [[0]*len(s) for i in range(len(s))]
            #filling out the diagonal by 1
            for i in range(len(s)):
                dp[i][i] = True
                pali = s[i]

            # fill the dp matrix
            for i in range(len(s)-1,-1,-1):
                # j starts from the i location : to only work on the upper side of the diagonal 
                for j in range(i+1,len(s)):  
                    if s[i] == s[j]:  #if the chars matches
                        # if len sliced substring is just one letter if the characters are equal, we can say they are palindomr dp[i][j] =True 
                        #if the slicied substring is longer than 1, then we should check if the inner string is also palindrom (check dp[i+1][j-1] is True)
                        if j-i ==1 or dp[i+1][j-1] is True:
                            dp[i][j] = True
                            # we also need to keep track of the maximum palindrom sequence 
                            if len(pali) < len(s[i:j+1]):
                                pali = s[i:j+1]

            return pali
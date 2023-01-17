class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        mapp=Counter(s)
        n=len(s)

        # we have counted number of zeros and ones
        # now our approach would be to keep track of left ones and right side zeros 
        # ie if 1 is on left or 0 is on right to keep an increasing sequence, we have to flip them.
        # if sumation of them is lowest at any index, we will get the ans.

        # to keep track of them at each index check each index
        # initally all zeros and ones would be on right side only
        # now if current is zero or one decrease right side zeros or ones, and increase left sides
        # now in meantime check if left ones and right zeros are minimum or not.

        lz,rz=0,mapp['0']
        lo,ro=0,mapp['1']
        minn=float('inf')
        for i in range(n):
            
            if s[i]=='0':
                rz-=1
                minn=min(minn, lo+rz)
                lz+=1
            else:
                ro-=1
                minn=min(minn, lo+rz)
                lo+=1
        return minn






















        # ones, ans = 0, 0                    # Example: s = "010110"
        #                                     #
        # for num in s:                       #  num    ones   ans  
        #                                     #  ––––   ––––   ––––  
        #     if num =='1': ones += 1         #    0      0     0
        #                                     #    1      1     0
        #     elif ones:                      #    0      0     1
        #         ones -= 1                   #    1      1     1
        #         ans += 1                    #    1      2     1
        #                                     #    0      1     2
        # return ans

        
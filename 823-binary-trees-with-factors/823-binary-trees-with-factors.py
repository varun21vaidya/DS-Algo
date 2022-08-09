class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
# first sort the array to get the numbers accordingly so we can take their mods with ease
# then use a map to use it as counter of freq of each values and each occuring value 
# will contribute to number of ways of binary tree
# now iterate over each number 
# to increase efficiency limit the loop upto square root of current num
# binary tree consist of a value/node compared with each value upto that value
# and if any of previous values can divide it to get int (factor A)
# and that int value is also present in arr upto current num (factor B)
# then num has both factor A and factor B as its leaf and it will be a binary tree
# and if both are same then only one way else it has 2 ways contributing to total ways
# as we move update the keys with ways and also the final ans regualrly with each iteration

        arr.sort()
        mapp, ans = dict(), 0
        for num in arr:
            ways, limit = 1, sqrt(num)
            for factorA in arr:
                if factorA > limit: break
                factorB = num / factorA
                if factorB in mapp:
                    ways += mapp[factorA] * mapp[factorB] * (1 if factorA == factorB else 2)
            mapp[num], ans = ways, (ans + ways)
        return ans % 1000000007
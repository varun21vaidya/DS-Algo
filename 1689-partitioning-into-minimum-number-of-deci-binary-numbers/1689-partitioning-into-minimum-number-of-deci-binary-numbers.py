class Solution:
    def minPartitions(self, n: str) -> int:
        # what is highest digit value in the given string 
        # like in 32 its 3, in 82734 its 8
        # so u need atleast that number of values
        # like for 3 it will need 1,1,1
        # for 8 will need 1,1,1...
        # so just return the max digit
        
        return max([int(a) for a in n])
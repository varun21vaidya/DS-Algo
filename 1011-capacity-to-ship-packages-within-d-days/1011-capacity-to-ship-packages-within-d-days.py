class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # check for this capacity if its useful for less than given days
        def check(cap):
            currwt,d=0,1
            for wt in weights:
                if currwt+wt>cap:
                    d+=1
                    currwt=wt
                else:
                    currwt+=wt
            
            return d<=days

        # #  Binary Search Solution:
        
        # first of all a ship should carry is any of the package 
        # so to get minimum capacity would be largest single package weight
        # and maximum a ship can carry is all of the packages ie it will take 1 day for it only
        # so we need to check optimum weight between them which satisfies day as given days
        # but same days does not mean capacity is minimum, cz for example 1, 16 would also need 5 days only
        # so after we get less than or eqaul to given days ie we should limit the capacity 
        # ie right = mid
        # and if the days required are more then we have assumed less capacity so we need to increase it
        # ie left = mid + 1
        # and just return left as ans 
        
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid= left+ (right-left)//2

            # if cap with this mid is less than or eqaul to days then
            # this is max optimal capacity and can be reduced further for minimum
            
            if check(mid):
                right=mid
            else:
                left=mid+1
            
        return left

        
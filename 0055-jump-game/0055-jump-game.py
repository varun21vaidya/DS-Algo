class Solution:
    def canJump(self, nums: List[int]) -> bool:
        move=1
        nums.pop()
        for num in nums:
            move-=1
            if num>move:
                move=num
            if move==0:
                return False
        return True
            

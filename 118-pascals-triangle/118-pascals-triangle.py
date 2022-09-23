class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums=[[1]*i for i in range(1,numRows+1)]
        print(nums)
        for i in range(2,numRows):
            for j in range(1,i):
                nums[i][j]=nums[i-1][j-1]+nums[i-1][j]
            # print(nums)
        return nums
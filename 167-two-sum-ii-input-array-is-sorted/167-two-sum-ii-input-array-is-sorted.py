class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # two pointer
        # i,j=0, len(numbers)-1
        # while i<j:
        #     if numbers[i]+numbers[j]==target:
        #         return [i+1,j+1]
        #     if numbers[i]+numbers[j]>target:
        #         j-=1
        #     else:
        #         i+=1
            
        # binary search
        for i in range(len(numbers)):
            low,high= i+1, len(numbers)-1
            while low<=high:
                mid=low+ (high-low)//2
                if numbers[mid]+numbers[i]==target:
                    return [i+1,mid+1]
                elif (numbers[mid]+numbers[i]>target):
                    high=mid-1
                else:
                    low=mid+1
                
            
            
            
                    
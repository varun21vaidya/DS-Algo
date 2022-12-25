class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        ans=[]
        for que in queries:
            add, size= 0,0
            for i in nums:
                if add+i<=que:
                    add+=i
                    size+=1
                else:
                    break
            ans.append(size)

        return ans
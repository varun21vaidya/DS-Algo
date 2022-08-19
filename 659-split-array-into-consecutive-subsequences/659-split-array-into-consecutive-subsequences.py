class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freqMap=Counter(nums)
        nextMap=Counter()
        for i in nums:
            if not freqMap[i]:
	            continue
            if nextMap[i]:
                    
                nextMap[i]-=1
                nextMap[i+1]+=1
            elif (freqMap[i+1] and freqMap[i+2]):
                freqMap[i+1]-=1
                freqMap[i+2]-=1
                
                nextMap[i+3]+=1
            else:
                return False
            freqMap[i]-=1
        return True
                